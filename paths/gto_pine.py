import pyautogui as pa
from time import sleep

def gto_pine():
    sleep(1)
    pa.press("e")
    pa.keyDown("d")
    pa.keyDown("s")
    sleep(0.65)
    pa.keyDown("space")
    pa.keyUp("space")
    sleep(0.1)
    pa.keyDown("space")
    pa.keyUp("space")
    sleep(7)
    pa.keyUp("s")
    sleep(9)
    pa.keyUp("d")