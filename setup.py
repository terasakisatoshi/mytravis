from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./tests')

setup(
    name="CITest",
    version="0.0.1",
    description="my first for travis ci",
    package=find_packages(),
    test_suite='test_myscript.suite')