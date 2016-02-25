#!/bin/bash

MAC_ARR=`sudo /bin/cat /home/djet/git/wifi_prob/text.txt | cut -d"_" -f1`
 echo '{'
 echo '    "data":['
for MAC in $MAC_ARR 
do
echo -n {\"{#WIFINAME}\":\"${MAC}\"},

# echo -n {\"{#WIFINAME}\":\"${MAC}\"}",
done
 echo -n {\"{#WIFINAME}\":\"FF:FF:FF:FF:FF:FF\"}
 echo -n ']'
 echo -n '}'
exit 0
