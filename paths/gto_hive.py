import pyautogui as pa
from time import sleep

def gto_hive():
    from sub_macro.macro import swalk, check_pixel, write_log
    sleep(0.4)
    pa.scroll(-50)
    pa.moveTo(x=340,y=118)
    swalk("w",3)
    swalk("s",0.5)
    swalk("d",3.5)
    pa.keyDown("a")
    while not check_pixel(796,70,238,238,242):
        sleep(0.001)
    pa.keyUp("a")
    pa.press("e")
    write_log("Collected hive.")