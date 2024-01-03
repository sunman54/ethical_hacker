import scapy.all as scapy

def get_mac(ip):    
    arp_request = sc.ARP(pdst = ip)
    broadcast = sc.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request # creating the packet
    answered_list, unanswered_list = sc.srp(arp_request_broadcast, timeout=2, verbose=False) #sending the packet

    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn= process_sniffed_packet)



def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
            
        try:    
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print('[x] You are UNDER ATTACK !!!')
                
        except IndexError:
            pass
    

sniff('eth0')
