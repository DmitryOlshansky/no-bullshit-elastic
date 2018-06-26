#!/usr/bin/env python3
# this is (more) then enough of dependencies
# to keep things nice, short and simple
import requests
import re
import json

time_pattern = re.compile(r"...TODO!...")

def evntes_from_file(file):
    accum = [] # accumulate here, yes, imperative accumulator shit, spot on ;)
    for line in file.readlines():
        if time_pattern.match(line):
            yield "\n".join(accum)
            accum = []
        else:
            accum.append(line)





