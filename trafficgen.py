#!/usr/bin/python
# This program uses the scapy library to send HTTP Get
# requests to a web server with forged src IPs
# This has the intention of making it more difficult for blue teams
# in cyber warfare games to identify the red teams IP

from scapy.all import *
src_ip = "10.1.20.38"
dst_ip = "10.1.20.1"
src_port = RandNum(1024, 65535)
dst_port = 80

dst_url = "www.google.com"
# Send the SYN
#syn = IP(dst=dst_url) / TCP(dport=dst_port, flags='S')
#syn

# Get the SYN-ACK
#syn_ack = sr1(syn)

#print "Received syn_ack: " + syn_ack
#getStr = "GET / HTTP/1.1\r\nHost: www.docs.kali.org\r\n\r\n"


#request = IP(dst=dst_url) / TCP(dport=dst_port, sport=syn_ack[TCP].dport,
#             seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr

#reply = sr1(request)
#print "Got reply: \n\t" + reply

#getRequest = IP(src=src_ip, dst=dst_url) / TCP(dport=dst_port) / getStr
#send(getRequest)

#reply = sr1(getRequest)
#print "Got GET request reply:\n\t"
#print getRequest

#Create SYN packet and send
ip = IP(dst=dst_url)
SYN = ip/TCP(sport=src_port, dport=dst_port, flags="S", seq=42)
print "Sending SYN \n"

# Receive SYN,ACK
SYNACK=sr1(SYN)
print "Receiving SYN,ACK \n"

# Create ACK packet
ACK=ip/TCP(sport=SYNACK.dport, dport=dst_port, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1)

print "Sending ACK Packet \n"
send(ACK)

print "Done!"











