import scapy.all as sc 
 

def scan(ip):
    
    arp_request = sc.ARP(pdst = ip)

    broadcast = sc.Ether(dst = 'ff:ff:ff:ff:ff:ff')

    arp_request_broadcast = broadcast/arp_request # creating the packet

    #print(arp_request.summary())

    #sc.ls(sc.ARP()) # list the parametter of ARP function

    answered_list, unanswered_list = sc.srp(arp_request_broadcast, timeout=2, verbose=False) #sending the packet

    print('IP Address\t\t\t\tMAC Adress')
    print('_'*60)

    for i in answered_list:
        #print(i[1].show())

        print(f'{i[1].psrc}\t\t\t\t{i[1].hwsrc}')

        #print(i[1].psrc) # ip of the device
        #print(i[1].hwsrc) # MAC of the device

    #arp_request_broadcast.show()
    #arp_request.show()
    #broadcast.show()




scan('192.168.232.1/24')