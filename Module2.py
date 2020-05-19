#!/usr/bin/env python3

import os
import requests
import json

inFolderPath = "/data/feedback/"
fileList = os.listdir(inFolderPath)
feedbackList = []
for file in fileList:
	feedbackDict = {}
	with open(inFolderPath + file, 'r') as f:
		title = f.readline().strip()
		feedbackDict["title"] = title
		name = f.readline().strip()
		feedbackDict["name"] = name
		date = f.readline().strip()
		feedbackDict["date"] = date
		feedback = f.read().strip()
		feedbackDict["feedback"] = feedback
	print(json.dumps(feedbackDict))
	r = requests.post("http://34.66.184.24/feedback/", data=feedbackDict)
	print(r.status_code)
