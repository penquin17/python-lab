# from https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
from setuptools import setup, find_packages

setup(
    name='extract',
    version='0.0.0',
    description='Extract data',
    author='penquin17',
    author_email='nquang.n17@gmail.com',
    packages=find_packages(include=['extract', 'extract.*']),
    # install_requires=[],
    # extras_require={
    #     'cuda': []
    # }
)
