#!/bin/bash
#
# Desc: Quickly discover your public IP
# 	Useful for confirming if a full IPv4 tunnel is working properly
#
###

curl -s 'http://checkip.dyndns.org' | sed 's/.*Current IP Address: \([0-9\.]*\).*/\1/g'
