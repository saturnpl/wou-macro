import subprocess
import pyautogui as pa
from json import load
from time import sleep
from datetime import datetime

now = datetime.now()
timer_done = False

def get_data():
    with open("sub_macro/settings.json", 'r') as f:
        data = load(f)
    return data
data = get_data()
def main():
    from main import save
    write_log("Started macro...")
    write_log("Checking if Sober is open or not...")
    save("running","0")
    if data["running"] == "0":
        from paths.gto_can import gto_cannon
        from paths.colhive import colhive
        window_id = get_sober_window()
        new_hive = False

        if window_id is not None:
            subprocess.run(
                ["wmctrl", "-i", "-a", window_id],
                capture_output=True,
                text=True
            )
            write_log("Sober is open.")
            sleep(0.4)
            reset()
            gto_cannon()

        else:
            write_log("Sober is not opened, opening it...")
            new_hive = True

            url = data["url"] or "roblox://experiences/start?placeId=1537690962"

            subprocess.Popen([
                "xdg-open",
                url
            ])

            while window_id is None:

                window_id = get_sober_window()

                if window_id is not None:
                    break

                sleep(1)

            subprocess.run(
                ["wmctrl", "-i", "-a", window_id],
                capture_output=True,
                text=True
            )

            sleep(3)

        write_log("Opened Sober.")

        if new_hive:
            write_log("Waiting until fully in bss.")
            found = False
            while True:
                pixel = pa.screenshot(region=(796, 519, 1, 1)).getpixel((0, 0))

                if not found:
                    if pixel == (50, 131, 255):
                        found = True
                else:
                    if pixel != (50, 131, 255):
                        break
            write_log("Bss has fully opnened. Collecting hive now.")
            colhive()

        gto_cannon()

def get_sober_window():
    write_log("Running wmctrl...")
    
    result = subprocess.run(
        ["wmctrl", "-l"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.splitlines():
        if "Sober" in line:
            return line.split()[0]

    return None

# only need a variable if its in a loop
def reset():
    sleep(1)
    pa.scroll(-100)
    pa.press("esc")
    pa.press("r")
    pa.press("enter")
    sleep(3)
    pa.scroll(-100)
    while check_pixel(1220, 774, 174, 64, 64):
        pa.press("esc")
        pa.press("r")
        pa.press("enter")
        sleep(3)
        pa.scroll(-100)


def swalk(key,seconds):
    with pa.hold(key):
        sleep(seconds)
def twalk(first_key,second_key,seconds):
    pa.keyDown(first_key)
    pa.keyDown(second_key)
    sleep(seconds)
    pa.keyUp(first_key)
    pa.keyUp(second_key)

def write_log(message):
    with open("log.txt", 'a') as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}\n")

def check_pixel(x,y,r,g,b):
    pixel = pa.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))
    return pixel == (r, g, b)
if __name__ == '__main__':
    main()

