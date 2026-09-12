import customtkinter as ctk
import json
from sub_macro import macro
import threading
import os
from sub_macro.macro import get_data, write_log
from pynput.keyboard import Key, Listener
from PIL import Image, ImageTk
from sys import platform


class Gui():
    root= None
    start_b = None
    stop_b = None

    def __init__(self):
        self.root = ctk.CTk()
        self.data = get_data()
        self.time_var = ctk.StringVar(value=self.data["time"])
        self.url_var = ctk.StringVar(value=self.data["url"])
        self.ms_var = ctk.StringVar(value=self.data["ms"])
        self.setup_window()
        self.setup_widgets()
        self.setup_hotkeys()
        if self.data["warning"] == "1":
            self.warning()

    def main(self):
        write_log("Started main.py")
        self.root.mainloop()

    def setup_window(self):
        self.root.geometry("500x300")
        self.root.title("Wou's macro")
        self.icon()

    def setup_widgets(self):
        self.tabs()
        self.optionmenu()
        self.entry()
        self.label()
        self.buttons()
        self.placew()
        self.vars()

    def icon(self):
        self.icon = Image.open("images/diamond_bee.png")
        self.photo = ImageTk.PhotoImage(self.icon)
        self.root.iconphoto(True,self.photo)

    def tabs(self):
        self.tv = ctk.CTkTabview(master=self.root, fg_color="transparent", width=500,height=300)
        self.tv.pack(fill="both", expand=True)
        self.tv.add("Gather")
        self.tv.add("Planter")
        self.tv.add("Boost")
        self.tv.add("Tad Sync") 
        self.tv.add("Settings") 

    def placew(self):
        self.start_b.place(y=270)
        self.stop_b.place(x=60,y=270)
        self.field.pack(anchor="nw")
        self.field.set(self.data["field"])
        self.gathertime.place(x=235)
        self.pattern.set(self.data["pattern"])
        self.pattern.place(x=150)
        self.url_text.place(x=0,y=0)
        self.url.place(x=75)
        self.hive_text.place(x=0,y=40)
        self.hive.set(self.data["hive_slot"])
        self.hive.place(x=77,y=40)
        self.ms_text.place(x=140,y=40)
        self.ms.place(x=235,y=40)
        self.version.place(relx=1.0,rely=1.0,anchor="se")
    def buttons(self):
        self.start_b = ctk.CTkButton(self.root,text="start(f1)",width=30,command=lambda: threading.Thread(target=macro.main, daemon=True).start())
        self.stop_b= ctk.CTkButton(self.root, text="stop(f2)",width=30,command=lambda: threading.Thread(target=self.restart, daemon=True).start())

    def setup_hotkeys(self):
        threading.Thread(target=self.listener,daemon=True).start()

    def optionmenu(self):
        self.field = ctk.CTkOptionMenu(master=self.tv.tab("Gather"), values=["Pine Tree", "Blue Flower Field", "Bamboo"], font=("bold", 13), width=145,command=self.field_option)
        self.pattern = ctk.CTkOptionMenu(master=self.tv.tab("Gather"), values=["Kettle", "Bff", "Bmb"], font=("bold", 13), width=80,command=self.pattern_option)
        self.hive = ctk.CTkOptionMenu(master=self.tv.tab("Settings"), values=["1","2","3","4","5","6"],font=("bold",10),width=60,command=self.hive_option)

    def vars(self):
        self.time_var.trace_add("write", lambda *args:self.save_time(self.time_var))
        self.url_var.trace_add("write", lambda *args:self.save_url(self.url_var))
        self.ms_var.trace_add("write", lambda *args:self.save_ms(self.ms_var))

    def entry(self):
        self.gathertime = ctk.CTkEntry(master=self.tv.tab("Gather"), width=43, textvariable= self.time_var)
        self.url = ctk.CTkEntry(master=self.tv.tab("Settings"), width=400, textvariable=self.url_var)
        self.ms = ctk.CTkEntry(master=self.tv.tab("Settings"), width=50, textvariable=self.ms_var)

    def label(self):
        self.url_text = ctk.CTkLabel(master=self.tv.tab("Settings"), text="Join link",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
        self.hive_text = ctk.CTkLabel(master=self.tv.tab("Settings"), text="Hive slot",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
        self.ms_text = ctk.CTkLabel(master=self.tv.tab("Settings"), text="Move Speed",fg_color="#333333",corner_radius=10,font=("bold", 13), text_color="#0A7199")
        self.version = ctk.CTkLabel(master=self.root, text="0.3.3", font=("bold",20),fg_color="#333333",corner_radius=10,text_color="#0A7199")


    def listener(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self,key):
        pass

    def warning(self):
        warning = ctk.CTkToplevel(self.root)
        warning.geometry("300x100")
        warning.title("WARNING!")

        warn_s = ctk.CTkLabel(
            warning,
            text="Before starting the macro,\nmake sure you have 100% SCALING!\n"
                "Or else the macro will not work correctly",
            font=("bold", 14),
            text_color="red"
        )
        warn_s.pack()

        never_show = ctk.CTkCheckBox(
            warning,
            text="Never show again",
            command=self.never_show_w
        )
        never_show.pack()

    def never_show_w(self):
        save("warning", "0")

    def never_show_os(self):
        save("oswarn", "0")

    def on_release(self, key):
        if key == Key.f1:
            self.root.after(0,self.start_b.invoke)
        elif key == Key.f2:
            self.root.after(0, self.stop_b.invoke)

    def restart(self):
        write_log("Stopped macro.")
        save("running","1")
        os.system("pkill python && sleep 0.3 && python /home/wou/Documents/python/macro/main.py")

    def field_option(self,choice):
        save("field",choice)

    def pattern_option(self,choice):
        save("pattern", choice)

    def hive_option(self,choice):
        save("hive_slot",choice)

    def save_time(self,time_var):
        save("time", time_var.get())

    def save_ms(self,ms_var):
        save("ms", ms_var.get())

    def save_url(self,url_var):
        save("url",url_var.get())

def save(key, value):
    with open("sub_macro/settings.json", "r") as f:
        data = json.load(f)

    data[key] = value

    with open("sub_macro/settings.json", "w") as f:
        json.dump(data, f, indent=4)



if __name__ == '__main__':
    save("running", "0")
    Gui().main()
    if platform == "linux" or platform == "linux2":
        pass
    else:
        data = get_data()
        if data["oswarn"] == "1":
            os_warnw = ctk.CTk()
            os_warnw.geometry("300x100")
            os_warnw.title("WRONG OS")
            os_warn = ctk.CTkLabel(os_warnw, text=f"You're running this on {platform}.\nThe macro was originally designed for Linux.",font=("bold",14), text_color="red")
            os_warn.pack()
            never_show = ctk.CTkCheckBox(os_warnw, text="Never show again", command=Gui.never_show_os)
            never_show.pack()
            os_warn.mainloop()