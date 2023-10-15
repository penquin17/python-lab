# from https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
from setuptools import setup, find_packages

setup(
    name='lab',
    version='0.1.0',
    description='Machine learning, deep learning and AI lab',
    author='penquin17',
    author_email='nquang.n17@gmail.com',
    packages=find_packages(include=['lab']),
)
