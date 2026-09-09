import pyautogui as pa
from time import sleep
import sys
from pathlib import Path

sleep(3)
def colhive():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from sub_macro.macro import check_pixel, write_log, get_data, reset
    from gto_can import gto_cannon
    data = get_data()
    if data["running"] == "0":
        print("going")
        sleep(0.4)
        pa.scroll(-100)
        pa.moveTo(x=340,y=118)
        pa.keyDown("w")
        while not check_pixel(1022, 78,247, 255, 249):
            sleep(0.01)
        pa.keyUp("w")
        pa.keyDown("d")
        while check_pixel(1022, 78,247, 255, 249):
            sleep(0.01)
        while not check_pixel(1022, 78,247, 255, 249):
            sleep(0.01)
        pa.keyUp("d")
        pa.keyDown("d")
        while check_pixel(1022, 78,247, 255, 249):
            sleep(0.01)
        while not check_pixel(1022, 78,247, 255, 249):
            sleep(0.01)
        pa.keyUp("d")
        pa.keyDown("a")
        while not check_pixel(883, 90, 247, 255, 249):
            sleep(0.01)
        pa.keyUp("a")
        pa.press("e")
        reset()
        write_log("Collected hive.")
        gto_cannon()