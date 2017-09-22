from setuptools import setup, find_packages
import sys

sys.append("./src")
sys.append("./tests")

setup(
    name="CITest",
    version="0.0.1",
    description="my first for travis ci",
    package=find_packages(),
    test_suite='test_myscript.suite')