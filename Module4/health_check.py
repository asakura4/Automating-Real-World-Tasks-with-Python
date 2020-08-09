#!/usr/bin/env python3

import os
import psutil
import shutil
import emails
import socket

MEM_THRESHOLD = 500 * 1024 * 1024
CPU_THRESHOLD = 80.0
DISK_THRESHOLD = 20.0





if __name__ == '__main__':
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	body = "the Connection Details Panel on the right hand side."	

	# CPU usage is over 80%
	if psutil.cpu_percent(interval=None) > CPU_THRESHOLD:
		subject = "Error - CPU usage is over 80%"
		message = emails.generate_error_report(sender, receiver, subject, body)
		emails.send_email(message)


	# Available disk space is lower than 20%
	du = shutil.disk_usage('/')
	free_disk = du.free/du.total * 100
	if free_disk < DISK_THRESHOLD:
		subject = "Error - Available disk space is less than 20%"
		message = emails.generate_error_report(sender, receiver, subject, body)
		emails.send_email(message)


	# Available memory is less than 500MB
	mem = psutil.virtual_memory()
	if mem.available < MEM_THRESHOLD:
		subject = "Error - Available memory is less than 500MB"
		message = emails.generate_error_report(sender, receiver, subject, body)
		emails.send_email(message)	


	# Hostname "localhost" cannot be resolved to "127.0.0.1"
	hostname = sockets.gethostbyname('localhost')
	if hostname != '127.0.0.1':
		subject = 'Error - localhost cannot be resolved to 127.0.0.1'
		message = emails.generate_error_report(sender, receiver, subject, body)
		emails.send_email(message)