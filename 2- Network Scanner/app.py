import scapy.all as sc 
import optparse



def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='target', help='Target IP / IP Range')
    options, arguments = parser.parse_args()
    return options

def scan(ip):
    
    arp_request = sc.ARP(pdst = ip)

    broadcast = sc.Ether(dst = 'ff:ff:ff:ff:ff:ff')

    arp_request_broadcast = broadcast/arp_request # creating the packet

    #print(arp_request.summary())

    #sc.ls(sc.ARP()) # list the parametter of ARP function

    answered_list, unanswered_list = sc.srp(arp_request_broadcast, timeout=2, verbose=False) #sending the packet


    client_list = []
    for i in answered_list:
        #print(i[1].show())

        client_dict = {'ip' : i[1].psrc, 'mac' : i[1].hwsrc}
        #print(f'{i[1].psrc}\t\t\t\t{i[1].hwsrc}')

        client_list.append(client_dict)

        #print(i[1].psrc) # ip of the device
        #print(i[1].hwsrc) # MAC of the device

    #arp_request_broadcast.show()
    #arp_request.show()
    #broadcast.show()

    #print(client_list)
    
    return client_list


def print_result(result):

    print('IP Address\t\t\t\tMAC Adress')
    print('-'*60)

    for i in result:
        print(f"{i.get('ip')}\t\t\t\t{i.get('mac')}")



options = get_arguments()

result = scan(options.target)
#result = scan('192.168.232.1/24')

print_result(result)