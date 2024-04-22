import argparse
import tempfile
import re
from urllib.request import urlretrieve
import subprocess
import sys
import os

def fetch_repo(url, version, dir):
    """
    This will download the tar.gz file of the repository and extract it to the specified directory.
    It will only untar the config and workflow directories.
    """
    # Check if version starts with 'v'
    # If so, remove it (is not included in the URL somehow)
    if re.match(r"^v", version):
        version = version[1:]
        
    target_url = f"{url}/archive/refs/tags/{version}.tar.gz"
    repo_name = url.split("/")[-1]
    
    # Download the tar.gz file in temp dir and untar to specified directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        print("Downloading tar.gz file...")
        download_file = os.path.join(tmpdirname, "target_repo.tar.gz")
        urlretrieve(target_url, download_file)
        
        print("Extracting config and workflow directories from tar.gz file...")
        subprocess.run([
            "tar", "-xzf", download_file, 
            "--wildcards", f"{repo_name}/config/*", f"{repo_name}/workflow/*",
            "--strip-components=1", f"--one-top-level={dir}"
            ])
        
        print("Done!")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "snakefetch",
                                     description = "Fetch config and workflow files from a Snakemake repository on GitHub",)
    parser.add_argument(
        "--dir", "-d",
        type=str,
        default="./",
        help="Directory to save the files to",
    )
    parser.add_argument(
        "--url", "-u",
        type=str,
        help="URL of the Snakemake repository on GitHub",
    )
    parser.add_argument(
        "--version", "-v",
        type=str,
        help="Release version of the Snakemake repository on GitHub",
    )
    
    args = parser.parse_args()

    