#!/bin/bash

while read line; do
	open -a /Applications/Firefox.app "$line"
done < file.txt
