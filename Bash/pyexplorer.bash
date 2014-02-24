#!/bin/bash
# a tool for analysis python package
# Author: Hung Nguyen Viet <hvnsweeting@gmail.com>
# Mon Feb 24 23:39:45 ICT 2014


dest=$1

if [ -z $dest ]; then
    echo "Usage: $0 destination"
    echo "Example: $0 ~/python2/lib/python2.7/site-packages/docutils"
    exit 1
fi

function separator {
  echo "========= $1 ========="
}

cd $dest
separator 'Total files '
find . -type f  -name '*.py' | wc -l
separator 'List of sub-dirs '
find . -type d
separator 'Top 20 longest files '
find . -name '*.py' -exec wc -l {} \; | sort -nr | head -n 20
separator 'All files/dirs in top dir (except *.pyc)'
find . -maxdepth 1 ! -name '*.pyc'

separator 'Top dir classes '
grep '^class' *.py | head -n 20
