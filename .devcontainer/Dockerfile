FROM mcr.microsoft.com/devcontainers/anaconda:latest

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
RUN mkdir -p /Users/Shared/Downloads
# Packages needed but part of base image include flask, jupyter, matplotlib, numpy, openpyxl, pandas, python, xlrd
RUN conda install category_encoders
RUN conda install graphviz
RUN pip install pyarrow 
RUN conda install python-graphviz
RUN pip install shap
RUN pip install sklearn
RUN pip install torch
RUN pip install torchtext
RUN pip install torchviz
RUN conda install torchvision

