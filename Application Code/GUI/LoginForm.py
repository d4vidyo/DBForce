import tkinter as tk
import customtkinter as ctk
import SQL

class login():    
    def __init__(self, master, settings, function):
        self.master = master
        self.settings=settings
        self.connection=None
        self.buildInput = function

        self.hostFrame = ctk.CTkFrame(master=master, fg_color = "transparent")
        self.hostFrame.pack(pady=10)
        self.hostLabel = ctk.CTkLabel(master=self.hostFrame, text="Host: ")
        self.hostLabel.pack(side="left", padx=5)
        self.hostText = tk.StringVar()
        self.hostText.trace("w", self.hostChanged)
        self.hostEntry = ctk.CTkEntry(master=self.hostFrame,placeholder_text="host", textvariable=self.hostText)
        self.hostEntry.pack()
        self.hostEntry.insert(0,settings.host)
        
        self.DBFrame = ctk.CTkFrame(master=master, fg_color = "transparent")
        self.DBFrame.pack(pady=10)
        self.DBLabel = ctk.CTkLabel(master=self.DBFrame, text="Database: ")
        self.DBLabel.pack(side="left", padx=5)
        self.DBText = tk.StringVar()
        self.DBText.trace("w", self.DBChanged)
        self.DBEntry = ctk.CTkEntry(master=self.DBFrame,placeholder_text="Database", textvariable=self.DBText)
        self.DBEntry.pack()
        self.DBEntry.insert(0,settings.DB)
        
        self.userFrame = ctk.CTkFrame(master=master, fg_color = "transparent")
        self.userFrame.pack(pady=10)
        self.userLabel = ctk.CTkLabel(master=self.userFrame, text="User: ")
        self.userLabel.pack(side="left", padx=5)
        self.userText = tk.StringVar()
        self.userText.trace("w", self.userChanged)
        self.userEntry = ctk.CTkEntry(master=self.userFrame,placeholder_text="User", textvariable=self.userText)
        self.userEntry.pack()
        self.userEntry.insert(0,settings.user)
        
        self.pwFrame = ctk.CTkFrame(master=master, fg_color = "transparent")
        self.pwFrame.pack(pady=10)
        self.pwLabel = ctk.CTkLabel(master=self.pwFrame, text="Password: ")
        self.pwLabel.pack(side="left", padx=5)
        self.pwText = tk.StringVar()
        self.pwText.trace("w", self.pwChanged)
        self.pwEntry = ctk.CTkEntry(master=self.pwFrame,placeholder_text="Password", show="*", textvariable=self.pwText)
        self.pwEntry.pack()
        self.pwEntry.insert(0,settings.pw)

        self.connect = ctk.CTkButton(master=master, text="Connect", command=self.connect)
        self.connect.pack(pady=20)

    def hostChanged(self, *args):
        self.settings.host = self.hostEntry.get()
            
    def DBChanged(self,*args):
        self.settings.DB = self.DBEntry.get()
            
    def userChanged(self,*args):
        self.settings.user = self.userEntry.get()
            
    def pwChanged(self,*args):
        self.settings.pw = self.pwEntry.get()


    def connect(self):
        self.disconnect()
        self.connection = SQL.connection()
        if self.connection.connect(self.settings) is None:
            return
        self.buildInput()

    def disconnect(self):
        if self.connection is None:
            return
        self.connection.disconnect()