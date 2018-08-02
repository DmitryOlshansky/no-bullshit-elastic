#!/bin/bash -e
# Use this run.sh to verify your programs and as basis for your run.sh / run.bat
# report timing from
# time ./run.sh

if [ $# -eq 0 ] ; then
	echo "Needs a single argument - path to folder with qa-[1-4].log files"
	exit 1
fi
folder=$1

curl -XDELETE '127.0.0.1:9200/*'

# time insertion, use total to report score
# ------------------------
# your program should go here
./parse-log.py  $folder/*.log
#----------------------------

# time forced refresh of index by 1 insertion + wait
curl -H 'Content-Type: application/json' '127.0.0.1:9200/contest/_doc/42?refresh=wait_for' --data '{ "ts" : 0, "message" : "msg"}'
