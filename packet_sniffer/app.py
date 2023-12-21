import scapy.all as sc
from scapy.layers import http


def sniff(interface):
    sc.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"HTTP Request: {url}")

        if packet.haslayer(sc.Raw):
            load = get_load(packet)
            print(f"Raw Data: {load}")


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_load(packet):
    return packet[sc.Raw].load

sniff("eno1")
