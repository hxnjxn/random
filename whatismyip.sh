#!/bin/bash
#
# Auth: Frank Cass showed me this
#
###

curl -s 'http://checkip.dyndns.org' | sed 's/.*Current IP Address: \([0-9\.]*\).*/\1/g'
