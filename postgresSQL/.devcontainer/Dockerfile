FROM mcr.microsoft.com/devcontainers/python:1-3.10-bullseye

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
COPY ../tutorial_container/requirements.txt .
RUN pip3 --disable-pip-version-check --no-cache-dir install -r ./requirements.txt 
# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



