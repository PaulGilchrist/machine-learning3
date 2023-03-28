# Setup and Run Steps

If using VSCode Dev Containers, all requirements will be setup for you.  Otherwise, you will need Python and Jupyter (or just MiniConda), and the list of python packages listed in the file `.devcontainer.Dockerfile`.

The `devcontainer.json` file has a mount point between the container and the `/Users/Shared/Downloads` folder on the host computer. If a different folder is used make sure to update the JSON file to reflect the different folder location or the removal of the mount point if the Jupyter notebook named `census_data_preprocessing.ipynb` will not be used.

## Requirements

* [Python](https://www.python.org) version 3 or greater
* [Jupyter notebook](https://jupyter-notebook.readthedocs.io/en/stable/) support
```bash
    pip install jupyter
    jupyter notebook
```
* [VS Code](https://code.visualstudio.com) (or equivalent IDE)
* Jupyter extension for VSCode

## Recommended
* Python virtual environment for this project
* [MiniConda](https://docs.conda.io/en/latest/miniconda.html)
