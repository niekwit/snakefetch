"""
Main module for snakefetch
"""

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
    It will only untar the config and workflow directories, unless specified otherwise.
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
        for directory in target_dirs.split(","):
            wildcards.append(f"{repo_name}/{directory}/*")

        # Construct tar command
        tar = ["tar", "-xzf", download_file, "--wildcards"]
        tar.extend(wildcards)
        tar.extend(["--strip-components=1", f"--one-top-level={out_dir}"])

        # Untar archive and extract only the config and workflow directories
        exit_code = subprocess.run(tar, check=False)

        if exit_code.returncode != 0:
            raise ValueError(f"""Failed to extract {target_dirs}
                             directories from tar.gz file
                             to {out_dir}""")
        print("Done!")
        return True


def main():
    """Main function for snakefetch.
    """

    # Command line parser
    msg = "Fetch config and workflow directories from a versioned Snakemake repository on GitHub"
    parser = argparse.ArgumentParser(prog = "snakefetch",
                                     description = msg,)
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
    h_msg = "Directories to fetch from the Snakemake repository on GitHub (default: %(default)s)"
    parser.add_argument(
        "--target-dirs", "-t",
        dest = "targetdirs",
        type = str,
        default = "config,workflow",
        help = h_msg,
    )
    parser.add_argument(
        "--version",
        action = "store_true",
        help = "Print snakefetch version and exit",
    )
    args = parser.parse_args()

    if args.version:
        print(f"snakefetch version {VERSION}")
        sys.exit(0)

    # Fetch repo directories
    fetch_repo(args.url, args.repoversion, args.outdir, args.targetdirs)
    