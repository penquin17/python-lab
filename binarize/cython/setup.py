from setuptools import Extension, setup
from Cython.Build import cythonize

ext = Extension(name="main", sources=["main.py"], extra_link_args=["-lm"])  # For Linux/macOS, "-lm" links to the math library

setup(
    name="main",
    ext_modules=cythonize(ext, compiler_directives={"language_level": "3"}),
)
