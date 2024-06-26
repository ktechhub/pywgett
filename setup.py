"""
A setuptools based setup module.
See:
https://www.ktechhub.com/tutorials/how-to-package-a-python-code-and-upload-to-pypi
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import io
from os import path, getenv
from setuptools import setup, find_packages

VERSION = getenv("VERSION", "0.0.3")  # package version
if "v" in VERSION:
    VERSION = VERSION[1:]

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with io.open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

REQUIRES_PYTHON = ">=3.6"

setup(
    name="pywgett",
    version=VERSION,
    packages=find_packages(exclude=["tests", "docs", ".github"]),
    install_requires=["click", "requests"],
    entry_points={
        "console_scripts": [
            "pywget = pywgett.cli:main",
        ],
    },
    test_suite="tests",
    python_requires=REQUIRES_PYTHON,
    author="Ktechhub",
    author_email="mm@ktechhub.com",
    description="Download utility as an easy way to get files from the net",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktechhub/pywgett",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="download utility wget pywgett pywget pywgett.py pywget.py",
    setup_requires=["wheel"],
    include_package_data=True,
)
