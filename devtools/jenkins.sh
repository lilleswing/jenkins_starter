#!/bin/bash
bash devtools/install.sh

export PATH=`pwd`/anaconda/bin:$PATH
source activate ml_starter

nosetests test_all.py
python my_experiment.py
