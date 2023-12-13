import subprocess as sb
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface name to chance its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')

    return parser.parse_args()

def change_mac(interface, new_mac):
    print(f'[+] Changing MAC Adress for {interface} to {new_mac}')
    
    sb.call(['ifconfig', interface, 'down'])
    sb.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    sb.call(['ifconfig', interface, 'up'])


options, argument = get_arguments()
change_mac(options.interface, options.new_mac)

print(f"[+] Success")
