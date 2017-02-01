#!/usr/bin/python
# This program uses the scapy library to send HTTP Get
# requests to a web server with forged src IPs
# This has the intention of making it more difficult for blue teams
# in cyber warfare games to identify the red teams IP

from scapy.all import *
src_ip = "192.168.20.20"
dst_ip = "10.1.20.1"
src_port = 6767
dst_port = 80

payload = "GET / HTTP 1.1"
packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port) / payload
send(packet)