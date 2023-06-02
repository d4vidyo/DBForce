import tkinter as tk
import customtkinter as ctk

class Table():
    def __init__(self, master, name, keyValues=[], values=[]):
        self.master = master
        self.name=name
        self.keyValues = values
        self.values = values

        self.keyItems = []
        self.items = []

        self.x=10
        self.y=10
        
        self.body = tk.Frame(master = master, back="#707070", highlightbackground="black", highlightthickness=2)
        self.body.place(x= self.x, y= self.y)
        self.setEvents(self.body, "body")


        self.titleFrame = tk.Frame(master=self.body, back ="#505050")
        self.titleFrame.pack(fill="both")
        self.setEvents(self.titleFrame, "titel")

        self.titel = ctk.CTkLabel(master=self.titleFrame, text = self.name, font=("Arial", 15))
        self.titel.pack(padx=20)
        self.setEvents(self.titel, "titel")

        self.titleDash = tk.Frame(master = self.body, height=2, back = "black")
        self.titleDash.pack(expand=True, fill = tk.BOTH)
        self.setEvents(self.titleDash, "body")

        for value in keyValues:
            label = ctk.CTkLabel(master=self.body, text=value)
            label.pack(pady=5, padx =5, fill="both", expand=True)
            self.setEvents(label, value)
            self.items.append(label)
            
        self.keyDash = tk.Frame(master = self.body, height=1, back = "black")
        self.keyDash.pack(expand=True, fill = tk.BOTH, padx=10)
        self.setEvents(self.keyDash, "body")


        for value in values:
            label = ctk.CTkLabel(master=self.body, text=value)
            label.pack(pady=5, padx =5, fill="both", expand=True)
            self.setEvents(label, value)
            self.items.append(label)
            
            
    def setEvents(self, target, name):
        target.bind('<ButtonPress-1>', lambda event, val=name: self.on_press(event, val))
        target.bind('<B1-Motion>', self.on_drag)
        target.bind('<ButtonRelease-1>', lambda event, val = name: self.on_release(event, val))

    def on_press(self, event, name):
        self.offset_x = event.x
        self.offset_y = event.y
        self.x = self.body.winfo_x()
        self.y = self.body.winfo_y()

    def on_drag(self, event):
        x = self.body.winfo_x() + event.x - self.offset_x
        y = self.body.winfo_y() + event.y - self.offset_y
        self.body.place(x=x, y=y)
        
    def on_release(self, event, name):
        if abs(self.body.winfo_x() - self.x) >=2:
            return
        if abs(self.body.winfo_y() - self.y) >=2:
            return
        print("clicked " + name)

    def destroy(self):
        self.body.destroy()
