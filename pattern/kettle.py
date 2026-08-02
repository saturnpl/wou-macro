import pyautogui as pa
from time import sleep
sleep(2)
def kettle():
    from sub_macro.macro import get_data, swalk, twalk
    data = get_data()
    m = 31/int(data["ms"])
    twalk('w','a',1)
    pa.press("1")
    pa.press("shift")
    pa.mouseDown()
    sleep(0.5)
    while True:
        swalk('a', 0.6)
        pa.press(',')
        swalk('a', 1.2)
        pa.press('.')
        swalk('d',  0.8)
        swalk('w', 0.6)



kettle()