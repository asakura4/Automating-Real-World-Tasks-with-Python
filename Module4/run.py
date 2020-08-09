#!/usr/bin/env python3

import os
import requests
import json

url = "http://34.67.163.152/fruits/"
inFolderPath = "/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))

fruitsDict = {}
for file in os.listdir(inFolderPath):
	if not file.endswith(".txt"):
		continue
	fruitsDict = {}
	with open(inFolderPath + file, 'r') as f:
		 name = f.readline().strip()
		 fruitsDict["name"] = name
		 weight = f.readline().split(' ')[0]
		 weight = int(weight)
		 fruitsDict["weight"] = weight
		 description = f.readline().strip()
		 fruitsDict["description"] = description
		 fruitsDict["image_name"] = file.split('.')[0] + ".jpeg"
	print(json.dumps(fruitsDict))
	r = requests.post(url, data=fruitsDict)
	print(r.status_code)