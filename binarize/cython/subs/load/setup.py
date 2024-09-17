# from https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
from setuptools import setup, find_packages

setup(
    name='load',
    version='0.0.0',
    description='Load data',
    author='penquin17',
    author_email='nquang.n17@gmail.com',
    packages=find_packages(include=['load', 'load.*']),
    # install_requires=[],
    # extras_require={
    #     'cuda': []
    # }
)
