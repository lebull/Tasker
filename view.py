from taskerconfig import TaskerConfig
from task import *

import Tkinter as tk
import tkFont
import tkFileDialog

"""
    TopView
        MainView
            InfoFrame
            TaskList
        AddView #Maybe should be named window?
"""


class TopView(tk.Toplevel):
    def __init__(self, master):

        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        ##---------- Menu Bar ----------##

        menubar = tk.Menu(self)
        self.configure(menu=menubar)

        self.fileMenu = tk.Menu(self)
        
        menubar.add_cascade(label="Window", menu=self.fileMenu)

        self.mainView = MainView(self)
        self.mainView.pack(fill=tk.BOTH, expand=1)

class MainView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)

        self.taskList = TaskList(self)
        self.taskList.pack(side='left', fill='both', anchor='w', expand=1)

        self.infoFrame = InfoFrame(self)
        self.infoFrame.pack(side='right', fill='both', anchor='e', expand=1)

class TaskList(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #Styling
        self.listFont = tkFont.Font(family="Helvetica", size=12)

        self.list = tk.Listbox(self, selectmode=tk.SINGLE, font=self.listFont)
        self.list.grid(row=0, column = 0)
        self.current = None

    def setTasks(self, data):
        self.list.delete(0, tk.END)

        for eachItem in data:
            self.list.insert(tk.END, str(eachItem))

class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)

        tk.Label(self, text="Name: ").grid(row=0, column=0, sticky='ne')        
        self.name = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.name.grid(row=0, column=1, sticky='nw' )

        tk.Label(self, text="Description: ").grid(row=1, column=0, sticky='ne')       
        self.description = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.description.grid(row=1, column=1, sticky='nw')

        tk.Label(self, text="Start Date: ").grid(row=2, column=0, sticky='ne')        
        self.start_date = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.start_date.grid(row=2, column=1, sticky='nw')

    def setInfo(self, inTask):
        self.name.config(text = str(inTask.name)        )
        self.description.config(text = str(inTask.description) )
        self.start_date.config(text = str(inTask.start_date)  )

class AddView(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.nameLabel = tk.Label(self, text="Name")
        self.nameLabel.pack()