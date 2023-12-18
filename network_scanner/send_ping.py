import scapy.all as sc 


def ping(ip):
    sc.arping(ip)



ping('192.168.232.1/24')