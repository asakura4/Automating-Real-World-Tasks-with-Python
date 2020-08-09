#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def generate_paragraph(folderPath):
	paragraph = ""
	br = "<br/>"
	for file in os.listdir(folderPath):
		if not file.endswith(".txt"):
			continue
		with open(folderPath + file, 'r') as f:
			name = f.readline().strip()
			paragraph = paragraph + "name: " + name + br
			weight = f.readline().strip()
			paragraph = paragraph + "weight: " + weight + br + br
	return paragraph



if __name__ == "__main__":
	now = datetime.datetime.now()
	title = "Procesed Update on {}".format(now.strftime("%B %d, %Y"))
	infolderPath = "/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))
	paragraph = generate_paragraph(infolderPath)
	if not os.path.exists('/tmp/'):
		os.makedirs('/tmp/')
	reports.generate_report("/tmp/processed.pdf", title, paragraph)
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. "
	body = body + "A detailed list is attached to this email."
	message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
	emails.send_email(message)