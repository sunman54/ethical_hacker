import subprocess as sb
import optparse

# interface = 'eth0'

# new_mac = '54:ee:dd:cc:bb:ff'

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface name to chance its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')
    options, argument = parser.parse_args()
    
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info')
    
    elif not options.new_mac:
        parser.error('[-] Please specify an MAC Address, use --help for more info')
    
    return options 

def change_mac(interface, new_mac):
    print(f'[+] Changing MAC Adress for {interface} to {new_mac}')
    
    sb.call(['ifconfig', interface, 'down'])
    sb.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    sb.call(['ifconfig', interface, 'up'])


options = get_arguments()
change_mac(options.interface, options.new_mac)

print(f"[+] Success")
