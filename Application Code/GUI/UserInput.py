import tkinter as tk
import customtkinter as ctk
import SQL

class input():
    def __init__(self, master, settings, connection, table, ER):
        self.master = master
        self.settings=settings
        self.connection = connection
        self.table=table
        self.ER = ER

        self.buildBase()

    def buildBase(self):
        self.button = ctk.CTkButton(master=self.master, text = "getData", command = self.btn)
        self.button.pack()

        self.schemaSelector()

    def schemaSelector(self):
        data = self.connection.getAllSchema()
        liste=[]
        for dta in data[1]:
            liste.append(dta[0])
        self.combobox = ctk.CTkComboBox(master = self.master, values = liste, command=self.onSchemaChange)
        self.combobox.pack(pady=10)
        data = self.connection.getCurrentSchema()
        self.combobox.set(data[1][0])

    def onSchemaChange(self, event):
        self.settings.Schema = "'"+event+"'"
        self.ER.buildSchemaTables()
                

    def btn(self):
        data = self.connection.get()
        self.table.build(data[0], data[1])
