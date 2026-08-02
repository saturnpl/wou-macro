import pyautogui as pa
from time import sleep
from sub_macro.macro import get_data, reset
from paths.gto_pine import gto_pine

def gto_cannon():
    data = get_data()
    m = 31/int(data["ms"])
    at_hive = True
    at_cannon = False
    sleep(5)
    reset(None)
    pa.scroll(-50)
    sleep(1)

    while not at_hive:
        sleep(3)
        reset(fl=at_hive)
    while not at_cannon:
        sleep(2)
        with pa.hold("w"):
            pa.sleep(1.3*m)
        sleep(0.4)
        if data["hive_slot"] == '1':
            with pa.hold("d"):
                pa.sleep(0.8/m)
        elif data["hive_slot"] == "2":
            with pa.hold("d"):
                pa.sleep(2*m)
        elif data["hive_slot"] == "3":
            with pa.hold("d"):
                pa.sleep(3.6*m)
        elif data["hive_slot"] == "4":
            with pa.hold("d"):
                pa.sleep(5*m)
        elif data["hive_slot"] == "5":
            with pa.hold("d"):
                pa.sleep(5.5*m)
        elif data["hive_slot"] == "6":
            with pa.hold("d"):
                pa.sleep(6.6*m) 
        else:
            with open('crash_log.txt', 'w') as f:
                f.write("Game crashed because hive slot number was either not set or doesn't exist.\n")
        sleep(0.3)
        pa.keyDown("space")
        pa.keyUp("space")
        pa.keyDown("d")
        sleep(1.3*m)
        pa.keyUp("d")
        sleep(0.5)
        try:
            pa.locateOnScreen("images/e.png", confidence=0.8)
            at_cannon = True
        except pa.ImageNotFoundException:
            reset(fl=None)

    if data["field"] == "Pine Tree":
        gto_pine()
    else:
        pass