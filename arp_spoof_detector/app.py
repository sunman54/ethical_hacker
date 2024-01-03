import scapy.all as scapy

# Function to retrieve MAC address associated with a given IP address
def get_mac(ip):
    arp_request = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request  # Create the ARP request packet
    answered_list, unanswered_list = sc.srp(arp_request_broadcast, timeout=2, verbose=False)  # Send the packet

    return answered_list[0][1].hwsrc

# Function to capture and process network packets on a specific interface
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

# Function to process captured network packets for ARP spoofing detection
def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print('[x] You are UNDER ATTACK !!!')

        except IndexError:
            pass

# Start capturing packets on 'eth0' interface
sniff('eth0')