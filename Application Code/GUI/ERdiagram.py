import tkinter as tk
import customtkinter as ctk
from GUI import ERtable
import SQL

class Diagram():
    def __init__(self, master):
        self.master=master
        self.tables = []
        self.connection = None

        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(expand=True, fill="both")

    def addConnection(self, connection):
        self.connection = connection
    
    def buildSchemaTables(self):
        data = self.connection.getAllTables()[1]

        TableNames=[]
        TableColumns = {}
        for name, value in data:
            if name in TableColumns:
                TableColumns[name].append(value)
            else:
             TableColumns[name] = [value]
             TableNames.append(name)
        print(TableNames)
        self.clearCanvas()
        for entry in TableNames:
            self.addTable(name =entry, values = TableColumns[entry])

    def addTable(self, name, values, keyValues=[]):
        newTable = ERtable.Table(self.canvas, name=name,keyValues=keyValues, values=values)


        self.tables.append(newTable)

    def clearCanvas(self):
        for table in self.tables:
            table.destroy()
