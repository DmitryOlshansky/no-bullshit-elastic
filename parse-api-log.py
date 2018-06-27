#!/usr/bin/env python3
# this is (more) then enough of dependencies
# to keep things nice, short and simple
import requests
import re
import json
import sys

time_pattern = re.compile(r"([0-9-]+\s*[0-9:.]+)(.*)")

accum = [] # accumulate here, yes, imperative accumulator shit, spot on ;)

for line in sys.stdin.readlines():
    result = time_pattern.match(line)
    if result:
        accum = [line] + accum
        event = " ".join(accum)
        accum = []
        ts = result.group(1)
        my_id = re.sub('[^A-Za-z0-9]+', '', ts)
        json_body = json.dumps({ "id" : my_id, "ts": ts, "text" : event })
        resp = requests.post("http://localhost:9200/siebel-3/log", headers={"Content-Type": "application/json"}, data=json_body)
        print("REQ | ID %s" % my_id)
        if resp.status_code >= 200 and resp.status_code < 300:
            print("*")
        else:
            print("Failed %s" % resp.status_code)
    else:
        accum.append(line)
