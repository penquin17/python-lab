# from https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
import os

from Cython.Build import cythonize
from setuptools import find_packages, setup

MAIN_PACKAGE = "loader"
ANCHOR = os.path.dirname(os.path.abspath(__file__))


def remove_py_files():
    for root, dirs, files in os.walk(os.path.join(ANCHOR, MAIN_PACKAGE)):
        for file in files:
            # Keep __init__.py if you want
            if file.endswith('.py') and file != '__init__.py':
                os.remove(os.path.join(root, file))


def create_init_files(base_dir):
    """Recursively creates __init__.py files in all directories within base_dir."""
    for root, dirs, files in os.walk(base_dir):
        if root.endswith("__pycache__"):
            continue
        # Create an __init__.py file in the current directory if it does not exist
        init_file_path = os.path.join(root, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as f:
                f.write("# This file was automatically generated.\n")
            print(f"Created {init_file_path}")
        else:
            print(f"'{init_file_path}' already exists.")


create_init_files(MAIN_PACKAGE)
setup(
    name='xt-utils',
    version='0.0.0',
    description='LIZAI XT utils',
    author='penquin17',
    author_email='will.nguyen@lizai.co',
    # packages=find_packages(include=['xt_utils', 'xt_utils.*']),
    # install_requires=[]
    # extras_require={
    #     'cuda': []
    # }
    ext_modules=cythonize(
        [
            os.path.join(ANCHOR, f"{MAIN_PACKAGE}/**/*.py")
        ],
        annotate=True,
        compiler_directives={'always_allow_keywords': True,
                             'language_level': "3", }),
)
