#!/bin/bash

scriptdir=$(dirname $(readlink -f $0))

prob=$1

if [ ! -d $scriptdir/$prob ]; then
    echo "Problem not found: $prob"
    exit 1
fi

export PYTHONPATH=$scriptdir/common 

time pypy $scriptdir/$prob/euler$prob.py

