import optparse
import scapy.all as sc
from scapy.layers import http
from urllib.parse import quote, unquote


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface_name', dest='interface', help='interface name  for watching the network traffic')
    options, argument = parser.parse_args()

    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info')

    elif not options.new_mac:
        parser.error('[-] Please specify an MAC Address, use --help for more info')

    return options


def sniff(interface):
    sc.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"[+] HTTP Request: {url}")

        if packet.haslayer(sc.Raw):
            load = get_load(packet)
            print(f"[+] Raw Data: {load}")


def get_url(packet):
    return unquote(packet[http.HTTPRequest].Host.decode("utf-8")) + unquote(packet[http.HTTPRequest].Path.decode("utf-8"))


def get_load(packet):
    return packet[sc.Raw].load.decode("utf-8")

options = get_arguments()
interface_name = options.interface
sniff(interface_name)
