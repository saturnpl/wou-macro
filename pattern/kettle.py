import pyautogui as pa
from time import sleep
from threading import Thread
def kettle():
    from sub_macro.macro import get_data, swalk, twalk
    data = get_data()
    countdown_thread = Thread(target=countdown)
    countdown_thread.start()
    if data["running"] == "0":
        twalk('w','a',1)
        pa.press("1")
        pa.press("shift")
        pa.mouseDown()
        sleep(0.5)
        while timer > 0:
            swalk('a', 0.6)
            pa.press(',')
            twalk("a","s",0.6)
            pa.press('.')
            swalk('d',  1.25)
            swalk('w', 0.6)

def countdown():
    from sub_macro.macro import get_data
    global timer
    data = get_data()
    sec = int(data["time"]) * 60
    timer = sec
    for x in range(sec):
        timer -= 1
        sleep(1)