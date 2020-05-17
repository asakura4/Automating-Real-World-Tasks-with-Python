'''
Qwiklabs Assessment: Scale and convert images using PIL
Introduction
Your company is in the process of updating its website, and they’ve hired a design contractor to 
create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format 
-- rotated 90° and too large. Oof! You’re not able to get in contact with the designers and your own deadline is approaching fast.
You’ll need to use Python to get these images ready for launch.

What you’ll do
Use the Python Imaging Library to do the following to a batch of images:

Open an image
Rotate an image
Resize an image
Save an image in a specific format in a separate directory
'''


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
	except:
		pass
