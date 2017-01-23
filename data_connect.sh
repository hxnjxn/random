#!/bin/sh
#
# Name: data_connect.sh
# Desc: Parse a copy and paste of a data.com employee contacts page into an email list
###

echo ""; echo "		-= data_connect.sh =-"; echo ""
echo "[*] Desc: This script will format a copy / paste of data.com contact names into an email list."
read -p "[*] Input a company email suffix (Eg. microsoft.com): " suffix
read -p "[*] Input the full path to the data_connect.txt file: " path
read -p "[*] Input a filename that you would like to output to: " filename
for i in $(cat $path  | awk '{$1=$1}{ print }' | sed 's/Direct Dial Available//g' | awk '{$1=$1}{ print }' | cut -d " " -f 1-2 | sed 's/, /./g' | sed 's/,//g'); do echo $i"@"$suffix >> $filename; done
echo "[*] Done. File saved to $filename"
