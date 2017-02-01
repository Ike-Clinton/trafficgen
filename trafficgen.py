#!/usr/bin/python
# This program uses the scapy library to send HTTP Get
# requests to a web server with forged src IPs
# This has the intention of making it more difficult for blue teams
# in cyber warfare games to identify the red teams IP

# Change log level to suppress annoying IPv6 error
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
 
# Import scapy
from scapy.all import *
 
# GET String
getStr = "GET / HTTP/1.0\r\nHOST: web.epi.com\r\n\r\n"
while True:
	# Set up target IP
	
	 
	# Generate random source port number
	port=RandNum(1024,65535)
	# Generate Random web traffic simulation to web.epi.com (192.168.20.20)
	rnd_src_ip = "" + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) 
	ip=IP(src=rnd_src_ip, dst="192.168.20.20")

	# Create SYN packet
	SYN=ip/TCP(sport=port, dport=80, flags="S", seq=0)
	 
	# Send SYN and don't wait for SYN,ACK since we won't get it due to random src.
	# timeout immediately.
	SYNACK=sr1(SYN, timeout = 0.25)
	 
	# Forge an ACK
	ACK=ip/TCP(sport=port, dport=80, flags="A", seq=1, ack=1) / getStr
	 
	# SEND our ACK packet
	print "\n[*] Sending ACK-GET packet"
	error,reply = sr(ACK, timeout=0.25)


	# Generate random IP and send SYN packets to 80, 3306, and 22
	rnd_src_ip = "" + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255))
	res, unans = sr( IP(src= rnd_src_ip, dst='192.168.20.20')/TCP(flags='S', dport=(80)), timeout = 0.25)
	rnd_src_ip = "" + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255))
	res, unans = sr( IP(src= rnd_src_ip, dst='192.168.20.21')/TCP(flags='S', dport=(3306)), timeout = 0.25)
	rnd_src_ip = "" + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255))
	res, unans = sr( IP(src= rnd_src_ip, dst='192.168.20.21')/TCP(flags='S', dport=(22)), timeout = 0.25)

	print res.summary()






