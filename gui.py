import threading
from tkcalendar import Calendar, DateEntry
from tkinter import ttk, Tk, Entry, Label, Text, END, Frame
import tkinter  as tk
from monitor import *
class Gui:
    def __init__(self):
        self.m = monitor()
        self.window = Tk()
        self.frameMonitor = Frame(self.window)
        self.frameManual = Frame(self.window)
        self.window.geometry("600x600")
        self.window.configure(bg="lightgray")
        self.time_text = Entry(self.frameMonitor)
        self.time=""
        self.stop_thread = True
        #inputs
        #Button
        ttk.Button(self.window, text="monitor", width=10, command=self.monitorShow).place(x=2, y=4)
        ttk.Button(self.window, text="manual", width=10, command=self.manualShow).place(x=100, y=4)
        self.date_start_entry = DateEntry(self.frameManual)
        self.date_end_entry = DateEntry(self.frameManual)
        self.date_start = self.date_start_entry.get()
        self.date_start = self.date_end_entry.get()
        # name button
        # self.name_button = Label(self.window, text="name:", bg="lightgray")
        # self.name_button.place(x=60, y=10)
        # self.name_button.config(font=("Ariel", 8))
        self.window.mainloop()


    def monitorShow(self):
        self.frameManual.pack_forget()
        self.frameMonitor.pack(side="top", expand=True, fill="both")
        self.msg_label1 = Text(self.frameMonitor)
        self.msg_label1.place(x=10, y=30, width=570, height=560)
        self.msg_label1.config(state="disabled")
        self.time_button = Label(self.frameMonitor, text="enter time in sec:", bg="lightgray")
        self.time_button.place(x=200, y=8)
        self.time_button.config(font=("Ariel", 8))
        self.time_text.place(x=300, y=8)
        ttk.Button(self.frameMonitor, text="ok", width=7, command=self.monitor).place(x=400, y=8)
    def monitor(self):
        self.time = int(self.time_text.get())
        threading.Thread(target=self.start).start()
        print((len(self.m.slist)))
        print("d")
        threading.Thread(target=self.recv).start()


    def start(self):
        self.m.start(self.time)

    def manualShow(self):
        self.frameMonitor.pack_forget()
        self.msg_label = Text(self.frameManual)
        self.msg_label.place(x=10, y=50, width=570, height=530)
        self.msg_label.config(state="disabled")
        self.frameManual.pack(side="top", expand=True, fill="both")
        self.date_start_entry.place(x=200, y=30)
        self.date_end_entry.place(x=200, y=10)


    def print(self, mes):
        self.msg_label1.config(state='normal')
        self.msg_label1.insert('end', mes)
        self.msg_label1.yview('end')
        self.msg_label1.insert('end', "\n")
        self.msg_label1.config(state='disable')
    def recv(self):
        print((len(self.m.slist)))
        while self.stop_thread:
            print("f")
            if len(self.m.slist) != 0:
                print("fdd")

                self.print(self.m.slist.pop(0))

if __name__ == '__main__':
    i = Gui()
