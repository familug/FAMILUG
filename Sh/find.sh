#!/bin/sh

# sh implementation of find command
# Usage
# $ sh ~/find.sh . init.yml
# Looking for directory init.yml
# Found init.yml in /home/hvn/me/elbisna/golang
# Found init.yml in /home/hvn/me/elbisna/jenkins2
# Found init.yml in /home/hvn/me/elbisna/prometheus
# Found init.yml in /home/hvn/me/elbisna/prometheus/node_exporter

# sh ~/find.sh . node_exporter
# Looking for  node_exporter

path=$1
filename=$2
cd $path
echo "Looking for filename:" $filename
sfind () {
    cd $1
    # echo "in $(pwd), got $1"
    for f in *; do
        # ./xyz -> xyz
        fn=$(basename "$f")
        # echo "  Checking $fn"
        if [ "$fn" = "$filename" ]; then
            echo "Found $fn in $(pwd)"
            # exit 0
        fi
        if [ -d "$f" ]; then
            sfind $fn $(pwd)
        fi
    done
    # echo "From $(pwd) back to: $2"
    cd $2
}

sfind $path $(pwd)
