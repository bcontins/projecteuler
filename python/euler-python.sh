#!/bin/bash

scriptdir=$(dirname $(readlink -f $0))

function execute {
    prob=$1
    fold=$(echo $prob | sed 's/\(.*\)[0-9]/\1/')

    if [ ! -d $scriptdir/$fold ]; then
        echo "Problem folder not found: $fold"
        exit 1
    fi

    if [ ! -f $scriptdir/$fold/euler$prob.py ]; then
        echo "Problem script not found: $fold/euler$prob.py"
        exit 1
    fi

    export PYTHONPATH=$scriptdir/

    time pypy $scriptdir/$fold/euler$prob.py
}

execute $1
