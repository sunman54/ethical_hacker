import subprocess as sb

# interface = 'eth0'

# new_mac = '54:ee:dd:cc:bb:ff'


try:

    interface = input("> Interface : ")
    new_mac = input("> New MAC Adress : ")

    print(f"[+] Chancing MAC address for {interface} to {new_mac}")


    sb.call(f'ifconfig {interface} down' , shell=True)
    sb.call(f'ifconfig {interface} hw ether {new_mac}' , shell=True)
    sb.call(f'ifconfig {interface} up' , shell=True)


    print(f"[+] Success")
    


except:
    print(f"[-] Task Failed")