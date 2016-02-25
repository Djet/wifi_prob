#!/bin/bash
MAC=$1

A=`sudo /bin/cat /home/djet/git/wifi_prob/text.txt | grep ${MAC} | cut -d"_" -f2`
if [ -z $A ]; then
echo 0
else
echo $A
fi

