import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "snakefetch",
    version = "0.5.1",
    py_modules=["snakefetch"],
    author = "Niek Wit",
    author_email = "nw416@cam.ac.uk",
    description = "Fetches workflow and config files from a Snakemake repository on GitHub",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/niekwit/snakefetch/tree/main",
    project_urls = {
        "Source": "https://github.com/niekwit/snakefetch/tree/main",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux', 
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10",
    entry_points = {
        "console_scripts": [
            "snakefetch = snakefetch:main"
        ]
    }
)