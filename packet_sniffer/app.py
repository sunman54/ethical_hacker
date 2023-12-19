import scapy.all as sc
from scapy.layers import http


def sniff(interface):
    sc.sniff(iface=interface, store=false, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)