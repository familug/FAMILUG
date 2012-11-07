#!/bin/bash

current_filename=$0

get_grandpa_dirname () {
    grandpaDir=$(dirname $0)
        for i in `seq $1` ; do
                grandpaDir=$(dirname $grandpaDir)
                done
}

get_grandpa_dirname 3
echo $grandpaDir
