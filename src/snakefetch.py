import argparse
import tempfile
import re
import subprocess
import os
import sys
from urllib.request import urlretrieve

VERSION = "0.5.1"

def fetch_repo(url, version, out_dir, target_dirs):
    """
    Download the tar.gz file of given repository and extract it to the specified directory.
    It will only untar the config and workflow directories.
    """        
    # Download the tar.gz file in temp dir and untar to specified directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        target_url = f"{url}/archive/refs/tags/{version}.tar.gz"
        print(f"Downloading archive file for version {version} from {url}...")
        download_file = os.path.join(tmpdirname, "target_repo.tar.gz")
        urlretrieve(target_url, download_file)
        
        print(f"Extracting config and workflow directories from tar.gz file to {out_dir}...")
        
        # Prepare repo name
        # Check if version starts with 'v'
        # If so, remove it (is not included in the archive somehow)
        if re.match(r"^v", version):
            version = version[1:]
            
        repo_name = url.split("/")[-1]
        repo_name = f"{repo_name}-{version}"
        
        # Prepare target directories command line argument(s)
        wildcards = []
        for d in target_dirs.split(","):
            wildcards.append(f"{repo_name}/{d}/*")
        
        # Construct tar command
        tar = ["tar", "-xzf", download_file, "--wildcards"]
        tar.extend(wildcards)
        tar.extend(["--strip-components=1", f"--one-top-level={out_dir}"])

        # Untar archive and extract only the config and workflow directories
        exit_code = subprocess.run(tar)
        
        if exit_code.returncode == 0:
            print("Done!")
            return True
        else:
            raise Exception(f"Failed to extract {target_dirs} directories from tar.gz file to {out_dir}")


def main():
    # Command line parser
    parser = argparse.ArgumentParser(prog = "snakefetch",
                                     description = "Fetch config and workflow directories from a versioned Snakemake repository on GitHub",)
    parser.add_argument(
        "--outdir", "-o",
        type = str,
        default = "./",
        help = "Directory to save the files to",
    )
    parser.add_argument(
        "--url", "-u",
        type = str,
        required = "--version" not in sys.argv,
        help = "URL of the Snakemake repository on GitHub",
    )
    parser.add_argument(
        "--repo-version", "-v",
        dest = "repoversion",
        type = str,
        required = "--version" not in sys.argv,
        help = "Release version of the Snakemake repository on GitHub",
    )
    parser.add_argument(
        "--target-dirs", "-t",
        dest = "targetdirs",
        type = str,
        default = "config,workflow",
        help = "Directories to fetch from the Snakemake repository on GitHub (default: %(default)s)",
    )
    parser.add_argument(
        "--version",
        action = "store_true",
        help = "Print snakefetch version and exit",
    )
    args = parser.parse_args()
    
    if args.version:
        print(f"snakefetch version {VERSION}")
        exit(0)
    
    # Fetch repo directories
    fetch_repo(args.url, args.repoversion, args.outdir, args.targetdirs)
    