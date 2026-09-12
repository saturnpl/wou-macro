import pyautogui as pa
from time import sleep
import sys
from pathlib import Path

sleep(2)
def gto_hive():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from sub_macro.macro import write_log, check_pixel, get_data
    data = get_data()
    if data["field"] == "Pine Tree" and data["pattern"] == "Kettle":
            pa.keyDown("s")
            pa.keyDown("d")
            while not check_pixel(1831, 320,56, 52, 51):
                sleep(0.01)
            pa.keyUp("s")
            pa.keyUp("d")
            pa.keyDown("a")
            while not check_pixel(472,132, 115,115,115):
                 sleep(0.01)
            pa.keyUp("a")
            pa.keyDown("w")
gto_hive()
