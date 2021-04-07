#!/bin/python3

from scapy.all import *
import sys
target=sys.argv[1]

print("TCP")
for i in range(1,31):
	packet=sr1(IP(dst=target,ttl=i)/TCP(dport=80,flags="S"),timeout=1, verbose=0)
	if packet is not None:
		if packet[IP].src!=None:
			print(i,packet[IP].src)
		if packet[IP].proto==6:
			if packet[TCP].flags.SA:
				print("Destination reached")
				break
	else:
		print(i,"*")		


