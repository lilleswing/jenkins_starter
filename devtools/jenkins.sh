#!/bin/bash
make install
export PATH=`pwd`/anaconda/bin:$PATH
source activate ml_starter

make run
