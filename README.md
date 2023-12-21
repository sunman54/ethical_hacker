

## 1 - MAC Changer
- An app that uses the ifconfig command to change the MAC address of a specified network interface
- Usage :
```console
sudo python3 change_mac.py -i <eth0> -m <54:ee:dd:cc:bb:ff>
```

## 2 - Network Scanner

- A simple network scanner using ARP (Address Resolution Protocol) to discover devices on a local network
- Usage :
```console
sudo ptyhon3 app.py -t <192.168.232.1/24>
```

## 3 - ARP Spoofer

- A basic implementation of a Man-in-the-Middle (MITM) attack using ARP spoofing. The script aims to intercept traffic between a target machine and a gateway by sending ARP spoofing packets
- Usage :
```console 
sudo ptyhon3 app.py -t <192.168.232.9> -g <192.168.232.1>
```

## 4- Packet Sniffer 

- An App that uses Scapy to sniff HTTP traffic on a specified network interface (interface_name). It captures packets and processes them to extract and print information about HTTP requests

- Usage :
  ```console
  sudo ptyhon3 app.py -i eth0
  ```

- test page : http://vbsca.ca/login/login.asp
- alternative page : http://testphp.vulnweb.com/login.php

