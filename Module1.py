#!/usr/bin/env python3

import os
from PIL import Image

inFolderPath = "/home/student-01-187b49f166c7/images/"
SIZE = (128, 128)
outFolderPath = "/home/student-01-187b49f166c7/opt/icons/"

if not os.path.exists('/home/student-01-187b49f166c7/opt/icons/'):
	os.makedirs('/home/student-01-187b49f166c7/opt/icons/')

for infile in os.listdir(inFolderPath):
	basename = os.path.basename(infile)
	outFile = outFolderPath + basename
	if infile.endswith(".DS_Store"):
		continue
	try:
		with Image.open(inFolderPath + infile) as im:
			new_im = im.convert('RGB').transpose(method=Image.ROTATE_90).resize(SIZE)
			new_im.save(outFile, "JPEG")
			print(outFile)
	except:
		pass