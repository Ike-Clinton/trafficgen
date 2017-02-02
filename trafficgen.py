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
getStr2 = "GET /wp-admin HTTP/1.0\r\nHOST: web.epi.com\r\n\r\n"
getStr3 = "GET /file-upload HTTP/1.0\r\nHOST: web.epi.com\r\n\r\n"

dst_ip = "192.168.20.20"

while True:
	# Set up target IP
	
	 
	# Generate random source port number
	port=RandNum(1024,65535)
	# Generate Random web traffic simulation to web.epi.com (192.168.20.20)
	rnd_src_ip = "" + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) 
	ip=IP(src=rnd_src_ip, dst=dst_ip)

	# Create SYN packet
	SYN=ip/TCP(sport=port, dport=80, flags="S", seq=0)
	 
	# Send SYN and don't wait for SYN,ACK since we won't get it due to random src.
	# timeout immediately.
	SYNACK=sr1(SYN, timeout = 0.25)
	# Forge an ACK
	ACK=ip/TCP(sport=port, dport=80, flags="A", seq=1, ack=1) / getStr
	 
	# SEND our ACK packet
	print "\n[*] Sending ACK-GET packet"
	error,reply = sr(ACK, timeout=0.1)


	# Generate random source port number
	port=RandNum(1024,65535)
	# Generate Random web traffic simulation to web.epi.com (192.168.20.20)
	rnd_src_ip = "" + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) + "." + str(RandNum(0, 255)) 
	ip=IP(src=rnd_src_ip, dst=dst_ip)

	# Create SYN packet
	SYN=ip/TCP(sport=port, dport=80, flags="S", seq=0)
	 
	# Send SYN and don't wait for SYN,ACK since we won't get it due to random src.
	# timeout immediately.

	SYNACK=sr1(SYN, timeout = 1)
	# Forge an ACK
	ACK=ip/TCP(sport=port, dport=80, flags="A", seq=1, ack=1) / getStr2

	# SEND our ACK packet
	time.sleep(RandNum(0,3))
	error,reply = sr(ACK, timeout=0.25)

	ACK=ip/TCP(sport=port, dport=80, flags="A", seq=1, ack=1) / getStr3
	 
	# SEND our ACK packet
	time.sleep(RandNum(0,3))
	error,reply = sr(ACK, timeout=0.25)

	print "Sending spoofed packets to 80, 3306, and 22"
	# Generate random IP and send SYN packets to 80, 3306, and 22
	for i in range(0, RandNum(10, 20)):
		# Send HTTP SYN 70% of the time
		num = RandNum(0, 10)
		if num > 2:
			rnd_src_ip = "" + str(RandNum(1, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(2, 254))
			res, unans = sr( IP(src= rnd_src_ip, dst=dst_ip)/TCP(flags='S', dport=(80)), timeout = 0.25)
			time.sleep(RandNum(0,1))

		# Send MySQL packet 40% of the time
		num = RandNum(0, 10)
		if num > 5:
			rnd_src_ip = "" + str(RandNum(1, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(2, 254))
			res, unans = sr( IP(src= rnd_src_ip, dst=dst_ip)/TCP(flags='S', dport=(3306)), timeout = 0.25)
			time.sleep(RandNum(0,1))

		# Send SSH packet 60% of the time
		num = RandNum(0, 10)
		if num > 3:
			rnd_src_ip = "" + str(RandNum(1, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(2, 254))
			res, unans = sr( IP(src= rnd_src_ip, dst=dst_ip)/TCP(flags='S', dport=(22)), timeout = 0.25)
			time.sleep(RandNum(0,1))
		# res, unans = sr( IP(src= "80.196.213.84", dst=dst_ip)/TCP(flags='S', dport=(80)), timeout = 0.25)


		for i in range(0, RandNum(10, 20)):
			# Send random packet 90% of the time 	
			num = RandNum(0, 10)
			if num > 1:
				rnd_src_ip = "" + str(10) + "." + str(RandNum(0, 254)) + "." + str(RandNum(0, 254)) + "." + str(RandNum(2, 254))
				res, unans = sr( IP(src= rnd_src_ip, dst=dst_ip)/TCP(flags='S', dport=(RandNum(20, 1024))), timeout = 0.25)

		# print res.summary() 






