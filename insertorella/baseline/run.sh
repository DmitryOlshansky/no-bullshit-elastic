#!/bin/bash
# Use this run.sh to verify your programs and as basis for your run.sh / run.bat
#

if [ $# -eq 0 ] ; then
	echo "Needs a single argument - path to folder with qa-[1-4].log files"
	exit 1
fi
folder=$1

./parse-log.py  $folder/*.log

curl 127.0.0.1:9200/contest/_refresh
