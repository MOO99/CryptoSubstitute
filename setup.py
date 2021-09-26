from setuptools import setup, find_packages

import cryptosubstitute

# META
__author__ = "Open Security Group"
# TODO author email
__version__ = cryptosubstitute.__version__
__package_name__ = "cryptosubstitute"
__description__ = "To be added"
__python_requires__ = ['', '']
__data_files__ = [("", ["LICENSE"])]
__url__ = "https://github.com/DarkSecDevelopers/CryptoSubstitute"

with open("README.md", "r") as readme:
    __long_description__ = readme.read()
