#!/bin/bash

INSTALL_MODE=${1:-install}

export DATE=`date +%Y-%m-%d`
export ENV_NAME=${ENV_NAME:-ml_starter}
export CPU_ONLY=${CPU_ONLY:-0}
export CONDA_URL=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

unamestr=`uname`
if [[ "$unamestr" == 'Darwin' ]];
then
   echo "Using OSX Conda"
   export CONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
   export CPU_ONLY=1
fi

export ENV_HASH=$(md5sum devtools/environment.yml | cut -f 1 -d " ")
if [[ -d "anaconda" && -f "devtools/${ENV_HASH}" ]];
then
    exit 0
else
    echo "Deleting Old Anaconda Repo"
    rm -rf anaconda
fi
touch "devtools/${ENV_HASH}"

export CONDA_EXISTS=`which conda`
if [[ "$CONDA_EXISTS" = "" ]];
then
    wget ${CONDA_URL} -O anaconda.sh;
    bash anaconda.sh -b -p `pwd`/anaconda
    export PATH=`pwd`/anaconda/bin:$PATH
else
    echo "Using Existing Conda"
fi

conda env create --name=${ENV_NAME} -f devtools/environment.yml

echo "Installed $ENV_NAME conda environment"
