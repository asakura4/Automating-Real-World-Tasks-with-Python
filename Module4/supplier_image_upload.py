#!/usr/bin/env python3
import requests
import os


url = "http://localhost/upload/"
inFolderPath = "/home/{}/supplier-data/images/".format(os.environ.get('USER'))

for file in  os.listdir(inFolderPath):
	if not file.endswith(".jpeg"):
		continue
	with open(inFolderPath + file, 'rb') as opened:
		r = requests.post(url, files={'file':opened})