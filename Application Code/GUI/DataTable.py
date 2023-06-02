import tkinter as tk
from tkinter import ttk
from types import NoneType
import customtkinter as ctk

class Table:
    def __init__(self, master):
        self.master = master

        self.scrollbar = ctk.CTkScrollbar(self.master, bg_color="white")
        self.scrollbar.pack(fill=tk.Y, side="right")

        self.treeView = ttk.Treeview(self.master, show="headings", yscrollcommand=self.scrollbar.set)
        self.treeView.pack(expand=True, fill = tk.BOTH)
        self.scrollbar.configure(command=self.treeView.yview)


    def build(self, headers, values=((),())):
        self.columCount = len(headers)
        self.entryCount = len(values)
        if len(values[0]) > self.columCount:
            print("wrong format")
            return

        self.treeView.destroy()

        self.treeView = ttk.Treeview(self.master,columns=headers, show="headings", yscrollcommand=self.scrollbar.set)
        self.treeView.pack(expand=True, fill = tk.BOTH)
        self.scrollbar.configure(command=self.treeView.yview)

        for header in headers:
            self.treeView.heading(header, text=header)
            
        for value in values:
            self.treeView.insert("", tk.END, values=value)

