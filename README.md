# lab
Machine Learning, Deep Learning and AI lab for learning & showcase purposes.

# Prerequisite 
- `conda`: for managing python packages
- add channels
    ```bash
    conda config --set channel_priority disabled
    conda config --append channels anaconda
    conda config --append channels conda-forge
    conda config --append channels plotly
    conda config --append channels pytorch
    conda config --append channels huggingface
    ```

# Installation
- create environment with `conda`
    ```bash
    conda create -n lab
    ```
- activate the environment
    ```bash
    conda activate lab
    ```
- install conda packages
    ```bash
    conda install -n lab --file conda-packages.txt
    ```
- install lab package in development mode
    ```bash
    conda install conda-build
    conda develop .
    ```
- install other packages that is not included by `conda` with `pip` (optional)
    ```bash
    pip install -r requirements.txt
    ```