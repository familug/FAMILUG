#!/bin/sh
#This script help autoshutdown your computer
$PASS = "MatKhau"

#sudo -S is use input from stdin
echo $PASS | sudo -S shutdown -h now
