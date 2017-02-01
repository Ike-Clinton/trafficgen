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
getStr = "GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n"

# Set up target IP
ip=IP(dst="www.google.com")
 
# Generate random source port number
port=RandNum(1024,65535)
 
# Create SYN packet
SYN=ip/TCP(sport=port, dport=80, flags="S", seq=42)
 
# Send SYN and receive SYN,ACK
print "\n[*] Sending SYN packet"
SYNACK=sr1(SYN)
print "\n[*] Receiving SYN,ACK packet"
 
# Create ACK packet
ACK=ip/TCP(sport=SYNACK.dport, dport=80, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1) / getStr
 
# SEND our ACK packet
print "\n[*] Sending ACK-GET packet"
error,reply = sr(ACK, multi=1, timeout=1)

print "Reply from server: \n"
for r in reply:
  print r.show()
 
print "\n[*] Done!"










