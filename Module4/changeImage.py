#!/usr/bin/env python3

import os 
from PIL import Image

inFolderPath = "/home/{}/supplier-data/images".format(os.environ.get('USER'))
NEW_SIZE = (600, 400)

for file in os.listdir(inFolderPath):
	if file.endswith(".DS_Store"):
		continue
	filePath = inFolderPath + file
	print(filePath)
	try:
		with Image.open(filePath) as im: 
			new_file, extension = os.path.splitext(file)
			new_filePath = inFolderPath + new_file + ".jpeg"
			im.convert('RGB').resize(NEW_SIZE).save(new_filePath, "JPEG")
	except:
		print("can not convert")