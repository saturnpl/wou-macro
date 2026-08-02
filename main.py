import customtkinter as ctk
import json
from sub_macro import macro
import threading
import os
from sub_macro.macro import get_data
from pynput.keyboard import Key, Listener

root= None
start_b = None
stop_b = None

def main():
    global root, start_b, stop_b
    data = get_data()
    if data["warning"] == "1":
        warning()
    root = ctk.CTk()
    root.geometry("500x300")
    root.title("Wou's macro")

    time_var = ctk.StringVar(value=data["time"])
    url_var = ctk.StringVar(value=data["url"])
    ms_var = ctk.StringVar(value=data["ms"])

    thread = threading.Thread(target=listener, args=())
    thread.daemon = True
    thread.start()

    tv = ctk.CTkTabview(master=root, fg_color="transparent", width=500,height=300)
    tv.place(x=0,y=0)
    tv.configure(anchor="nw")

    tv.add("Gather")
    tv.add("Planter")
    tv.add("Boost")
    tv.add("Tad Sync") 
    tv.add("Settings") 

    start_b = ctk.CTkButton(root,text="start(1)",width=30,command=lambda: threading.Thread(target=macro.main, daemon=True).start())
    start_b.place(y=270)
    stop_b= ctk.CTkButton(root, text="stop(2)",width=30,command=lambda: threading.Thread(target=restart, daemon=True).start())
    stop_b.place(x=60,y=270)

    field_text = ctk.CTkLabel(master=tv.tab("Gather"), text="Field",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
    field_text.place(x=0,y=0)
    field = ctk.CTkOptionMenu(master=tv.tab("Gather"), values=["Pine Tree", "Blue Flower Field", "Bamboo"], font=("bold", 10), width=135,command=field_option)
    field.pack(anchor="nw",padx=60)
    field.set(data["field"])

    gathertime_text = ctk.CTkLabel(master=tv.tab("Gather"),text="Time",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
    gathertime_text.place(x=200)
    gathertime = ctk.CTkEntry(master=tv.tab("Gather"), width=43, textvariable= time_var)
    time_var.trace_add("write", lambda *args:save_time(time_var))
    gathertime.place(x=260)

    url_text = ctk.CTkLabel(master=tv.tab("Settings"), text="Join link",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
    url_text.place(x=0,y=0)
    url = ctk.CTkEntry(master=tv.tab("Settings"), width=400, textvariable=url_var)
    url_var.trace_add("write", lambda *args:save_url(url_var))
    url.place(x=75)

    hive_text = ctk.CTkLabel(master=tv.tab("Settings"), text="Hive slot",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
    hive_text.place(x=0,y=40)
    hive = ctk.CTkOptionMenu(master=tv.tab("Settings"), values=["1","2","3","4","5","6"],font=("bold",10),width=60,command=hive_option)
    hive.set(data["hive_slot"])
    hive.place(x=77,y=40)

    ms_text = ctk.CTkLabel(master=tv.tab("Settings"), text="Move Speed",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
    ms_text.place(x=140,y=40)
    ms = ctk.CTkEntry(master=tv.tab("Settings"), width=50, textvariable=ms_var)
    ms_var.trace_add("write", lambda *args:save_ms(ms_var))
    ms.place(x=235,y=40)

    root.mainloop()

def listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def on_press(key):
    pass

def warning():
    warning = ctk.CTk()
    warning.geometry("300x100")
    warning.title("WARNING!")
    warn_s = ctk.CTkLabel(warning, text="Before starting the macro,\n make sure you have 100% SCALING!\n Or else the macro will not work correctly", font=("bold",14), text_color="red")
    warn_s.pack()

    never_show = ctk.CTkCheckBox(warning, text="Never show again", command=never_show_w)
    never_show.pack()

def never_show_w():
    save("warning", "0")

def on_release(key):
    if key == Key.f1:
        root.after(0,start_b.invoke)
    elif key == Key.f2:
        root.after(0, stop_b.invoke)

def restart():
    os.system("pkill python && sleep 0.3 && python /home/wou/Documents/python/macro/main.py")

def field_option(choice):
    save("field",choice)

def hive_option(choice):
    save("hive_slot",choice)

def save_time(time_var):
    save("time", time_var.get())

def save_ms(ms_var):
    save("ms", ms_var.get())

def save_url(url_var):
    save("url",url_var.get())

def save(key, value):
    with open("sub_macro/settings.json", "r") as f:
        data = json.load(f)

    data[key] = value

    with open("sub_macro/settings.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    save("running", "0")
    main()