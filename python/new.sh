#!/bin/bash

scriptdir=$(dirname $(readlink -f $0))

prob=$1

if [ -d $scriptdir/$prob ]; then
    echo "Aleardy exists: $prob"
    exit 1
fi

cd $scriptdir

last=`ls -1 | grep -e "^...$" | tail -n 1`

cd -

mkdir -v $scriptdir/$prob

cp -v $scriptdir/$last/euler$last.py $scriptdir/$prob/euler$prob.py

gedit $scriptdir/$prob/euler$prob.py &

