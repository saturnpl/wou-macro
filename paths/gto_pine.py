import pyautogui as pa
from time import sleep

def gto_pine():
    from sub_macro.macro import write_log, check_pixel
    from pattern.kettle import kettle
    write_log("Going to Pine Tree.")
    sleep(1.5)
    pa.press("e")
    pa.keyDown("d")
    pa.keyDown("s")
    sleep(0.65)
    pa.keyDown("space")
    pa.keyUp("space")
    sleep(0.1)
    pa.keyDown("space")
    pa.keyUp("space")
    while not check_pixel(1456, 703,41,38,38):
            sleep(0.1)
    pa.keyUp("s")
    pa.keyUp("d")
    write_log("Arrived at Pine Tree.")
    write_log("Starting kettle pattern.")
    kettle()
