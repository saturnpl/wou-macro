import pyautogui
from time import sleep

def s():
    while 1:
        x, y = pyautogui.position()
        r,g,b = pyautogui.pixel(x, y)
        print(f"rgb:{r,g,b}")
        print(f"pos:{x,y}")
        sleep(2)
        #with open("random.txt", 'a') as f:
            #f.write(f"pos: {x,y}, rgb: {r,g,b}\n")

#50 131 255

#color = (25,46,77)
def w():
    color=(238, 238, 242)
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                print("found")

def d():
    while True:
        pixel = pyautogui.screenshot(region=(796, 70, 1, 1)).getpixel((0, 0))
        print("Actual:", pixel)
        if pixel == (238, 238, 242):
            print("found")
        else:
            print("not found")
        sleep(0.5)

def color_exists(pos1, pos2, rgb):
    img = pyautogui.screenshot(
        region=(
            pos1[0],
            pos1[1],
            pos2[0] - pos1[0] + 1,
            pos2[1] - pos1[1] + 1
        )
    )

    return any(
        img.getpixel((x, y))[:3] == rgb
        for x in range(img.width)
        for y in range(img.height)
    )

s()
