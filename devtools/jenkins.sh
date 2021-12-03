#!/bin/bash
if ! [ -x "$(command -v make)" ]; then
  echo 'Warning Make Not Installed Using Bash'
  bash devtools/install.sh
else
  make install
fi

export PATH=`pwd`/anaconda/bin:$PATH
source activate ml_starter

df > tmp.txt

make all
