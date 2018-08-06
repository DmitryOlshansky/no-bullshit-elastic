#!/bin/bash
#

if [ $# -eq 0 ] ; then
	echo "Needs a single argument - path to folder with qa-[1-4].log files"
	exit 1
fi
folder=$1

for file in $folder/*.log ; do
	awk -f parser.awk < $file &
done

wait
