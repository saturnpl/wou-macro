import pyautogui as pa
from time import sleep, time
from sub_macro.macro import get_data, reset, write_log, swalk,check_pixel
from paths.gto_pine import gto_pine

def gto_cannon():
    from main import save
    save("running", "1")
    data = get_data()
    m = 31/int(data["ms"])
    at_hive = True
    at_cannon = False
    reset()
    pa.scroll(-50)
    pa.moveTo(x=340,y=118)
    sleep(1)
    write_log("Going to cannon.")
    while not at_hive:
        sleep(1)
        reset()
    while not at_cannon:
        sleep(0.3)
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
            write_log("Game crashed because hive slot number was either not set or doesn't exist.")
        sleep(0.3)
        write_log("Going to cannon.")
        pa.keyDown("d")
        sleep(0.6)
        pa.keyDown("space")
        pa.keyUp("space")
        sleep(0.1)
        pa.keyDown("space")
        pa.keyUp("space")
        sleep(0.4)
        pa.keyDown("space")
        pa.keyUp("space")
        while not check_pixel(796, 70,238, 238, 242):
            sleep(0.1)
        pa.keyUp("d")
        write_log("Found Cannon")
        at_cannon = True


        
    if data["field"] == "Pine Tree":
        gto_pine()
    else:
        pass