
from os import path
import setuptools
from setuptools import setup
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements


WORKING_DIR = path.abspath(path.dirname(__file__))

# Get the long description from the README.md
with open(path.join(WORKING_DIR, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    author='Dave Gallant',
    author_email='davegallant@gmail.com',
    description='a class decorator that applies to all methods',
    keywords=['methods', 'decorator'],
    license='Apache License, Version 2.0',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    name='decorate-all-methods',
    packages=setuptools.find_packages(),
    url='https://github.com/davegallant/decorate_all_methods',
    version='0.0.2',
)
