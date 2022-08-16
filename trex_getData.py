import keyboard
import uuid
import time
from PIL import Image
from mss import mss


mon = {"top":350, "left":735, "width":250, "height":100}
sct = mss()

i = 0

def record_screen(record_id, key):
    global i

    i += 1
    print("{} :{}".format(key,i))
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key, record_id, i))

is_Exit = False

def exit():
    global is_Exit
    is_Exit = True


keyboard.add_hotkey("esc", exit)

record_id = uuid.uuid4()

while True:

    if is_Exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id, "up")
            time.sleep(0.3)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.3)
        elif keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.3)
    except RuntimeError: continue



























