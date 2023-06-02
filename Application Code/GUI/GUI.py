import tkinter as tk
import customtkinter as ctk
import time
from GUI import DataTable
from GUI import UserInput
from GUI import ERdiagram
from GUI import LoginForm
import SQL

class Window:
    def __init__(self, settings):
        self.settings = settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.buildWindow()
        self.buildMainFrame()
        self.populateFrames()
        
        
    def buildWindow(self):        
        self.root = ctk.CTk()
        self.root.geometry("1120x630")
        self.root.title(self.settings.Name)
        #self.root.iconbitmap("Images/exeIcon.ico")        


    def buildMainFrame(self):
        self.paneMaster = tk.PanedWindow(self.root, orient=tk.VERTICAL, sashpad=8, sashrelief=tk.RAISED)
        self.paneMaster.pack(expand=True, fill=tk.BOTH)

        self.tableFrame= ctk.CTkFrame(master = self.paneMaster)
        self.paneMaster.add(self.tableFrame)

        self.secondFrame= ctk.CTkFrame(master = self.paneMaster)
        self.paneMaster.add(self.secondFrame)

        self.paneSecondary = tk.PanedWindow(self.secondFrame, orient = tk.HORIZONTAL, sashpad=8, sashrelief=tk.RAISED)
        self.paneSecondary.pack(expand=True, fill=tk.BOTH)

        self.extraFrame = ctk.CTkFrame(master = self.paneSecondary)
        self.paneSecondary.add(self.extraFrame)

        self.tabView = ctk.CTkTabview(master = self.extraFrame)
        self.tabView.pack(expand=True, fill="both")
        self.tabView.add("Login")

        self.inputFrame = ctk.CTkFrame(master=self.root, fg_color="transparent")

        self.loginFrame = ctk.CTkFrame(master=self.tabView.tab("Login"), fg_color="transparent")
        self.loginFrame.pack(expand=True, fill="both")
        
        self.ER_Frame = ctk.CTkFrame(master=self.paneSecondary)
        self.paneSecondary.add(self.ER_Frame)

    def populateFrames(self):
        self.table = DataTable.Table(self.tableFrame)
        self.login = LoginForm.login(self.loginFrame, self.settings, self.populateInput)
        self.ER = ERdiagram.Diagram(self.ER_Frame)
        

    def populateInput(self):
        try:
            self.tabView.add("SQL")
        except(Exception)as e:
            print(e)

        self.ER.addConnection(self.login.connection)
        self.ER.buildSchemaTables()

        self.inputFrame.destroy()
        self.inputFrame = ctk.CTkFrame(master=self.tabView.tab("SQL"), fg_color="transparent")
        self.inputFrame.pack(expand=True, fill="both")
        self.input = UserInput.input(self.inputFrame, self.settings, self.login.connection, self.table, self.ER)
        self.tabView.set("SQL")


    def run(self):
        while True:
            time.sleep(self.settings.frametime)
            self.update()

    def update(self):
        self.root.update()

