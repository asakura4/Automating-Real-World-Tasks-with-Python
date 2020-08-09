#!/usr/bin/env python3
import requests

# This example shows hoa a file can be uploaded using the Python Requests module

url = "http://localhost/upload/"
with open('usr/share/apache2/icond/icon.sheet.png', 'rb') as opened:
	r = requests.post(url, files={'file':opened})