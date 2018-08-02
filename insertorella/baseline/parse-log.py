#!/usr/bin/env python3
# This is (more) then enough of dependencies for 
# very fast import from Python3 .. in "script" league,
# not in "as fast as C" league

import requests
import regex # better & faster regex module then `re`
import json
import sys
from multiprocessing import Pool

time_pattern = regex.compile(r"^([0-9-]+\s*[0-9:.]+)(.*)")
events_per_bulk = 10

def insert(bulk):
    # using bulk API is key to fast indexing
    resp = requests.post("http://127.0.0.1:9200/_bulk", headers={ 'Content-Type' : 'application/json'}, data=bulk)
    if resp.status_code < 200 or resp.status_code > 300:
        print("Failed to insert, %s" % resp.text)

def process_log(src):
    accum = "" # build our JSON request here
    count = 0
    err = 0
    with open(src) as f:
        bulk_accum = ""
        for line in f.readlines():
            # Python regex sucks
            result = time_pattern.match(line)
            if result and len(accum) > 0: # on first line accum == 0
                count += 1
                event = accum
                accum = line
                ts = result.group(1)
                bulk_accum += json.dumps({ "index" : { "_index" : "contest", "_type" : "_doc" } }) + "\n" \
                    + json.dumps({"ts" : ts, "text":  event }) + "\n"
                if count % events_per_bulk == 0:
                    print("%s - %d events parsed." % (src, count))
                    insert(bulk_accum)
                    bulk_accum = ""
            else:
                accum += line
    # insert leftover
    if bulk_accum != "":
        insert(bulk_accum)
    return count, err

files = sys.argv[1:]
pool = Pool(len(files))
pairs = pool.map(process_log, files)
total = 0 
for i, p in enumerate(pairs):
    total += p[0]
    print("Done %d: %s/%s" % (i, p[0] - p[1], p[0]))
print("Total docs: %d" % total)
