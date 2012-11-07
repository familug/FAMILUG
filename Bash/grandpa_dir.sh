#!/bin/bash

get_grandpa_dirname () {
    echo $1
    grandpaDir=$(dirname $0)
    # convert it to absolute path
    grandpaDir=$(cd $grandpaDir && pwd)

    for i in `seq $1` ; do
        grandpaDir=$(dirname $grandpaDir)
    done
    echo $grandpaDir
}

get_grandpa_dirname 3
echo $grandpaDir
