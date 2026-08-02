import subprocess
import pyautogui as pa
from json import load, dump
from time import sleep
def get_data():
    with open("sub_macro/settings.json", 'r') as f:
        data = load(f)
    return data
data = get_data()
m = 31/int(data["ms"]) #m short for multiplier
def main():
    from main import save
    if data["running"] == "0":
        from paths.gto_can import gto_cannon
        window_id = "0x04a00031"
        subprocess.run(["wmctrl", "-i", "-a", window_id])
        gto_cannon()
        save("running", "1")

# only need a variable if its in a loop
def reset(fl):
    sleep(3)
    pa.press('esc')
    pa.press('r')
    pa.press('enter')
    sleep(3)
    if fl == None:
        try:
            pa.locateOnScreen("images/brown.png", confidence=0.8)
            pa.press('esc')
            pa.press('r')
            pa.press('enter')
        except pa.ImageNotFoundException:
            pa.scroll(-50)
    else:
        while fl:
            try:
                pa.locateOnScreen("images/brown.png", confidence=0.8)
                pa.press('esc')
                pa.press('r')
                pa.press('enter')
            except pa.ImageNotFoundException:
                pa.scroll(-50)
                fl = False

def swalk(key,seconds):
    with pa.hold(key):
        if int(data["ms"]) >= 1:
            sleep(seconds*m)
        else:
            sleep(seconds/m)
def twalk(first_key,second_key,seconds):
    pa.keyDown(first_key)
    pa.keyDown(second_key)
    if int(data["ms"]) >= 1:
        sleep(seconds*m)
    else:
        sleep(seconds/m)
    pa.keyUp(first_key)
    pa.keyUp(second_key)

