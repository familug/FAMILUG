#!/bin/sh
#This script help autoshutdown your computer
#To run this, change it to executable
#use "chmod a+x shutdown.sh"
PASS="MatKhau"

#sudo -S is use input from stdin
echo $PASS | sudo -S shutdown -h now
