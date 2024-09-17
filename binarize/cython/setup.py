# setup.py
import os
from setuptools import setup
from Cython.Build import cythonize


def remove_py_files():
    for root, dirs, files in os.walk('src'):
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


MAIN_PACKAGE = "src"

create_init_files(MAIN_PACKAGE)

# Automatically compile all .py files in the core package recursively
setup(
    ext_modules=cythonize(f"{MAIN_PACKAGE}/**/*.py", language_level="3",
                          compiler_directives={'always_allow_keywords': True}),
)
