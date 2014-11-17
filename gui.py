"""
  TODO:
    -Pull in global model
    -Minimize to system tray 
      -http://www.blog.pythonlibrary.org/2013/07/12/wxpython-how-to-minimize-to-system-tray/

"""

import ttk

import Tkinter as tk
import tkFileDialog
#import wx

from taskerconfig import TaskerConfig
from task import *

model = {}
model['tasks'] = Task.getAllTasks()
model['selected_task'] = None

class Observable:
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def addCallback(self, func):
        self.callbacks[func] = 1

    def delCallback(self, func):
        del self.callback[func]

    def _docallbacks(self):
        for func in self.callbacks:
             func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None


class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):

        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")

        self.model = model

      #Call the parent init
        tk.Tk.__init__(self, *args, **kwargs)

        #Do we even need this?
        self.windows = []

        ##---------- Menu Bar ----------##

        menubar = tk.Menu(self)
        self.configure(menu=menubar)

        fileMenu = tk.Menu(self)
        fileMenu.add_command(label="New Task", command=self.add_task)

        menubar.add_cascade(label="Window", menu=fileMenu)

        ##---------- Main Layout ----------##

        self.taskList = TaskList(self)
        self.taskList.grid(row=0, column=0)
        self.taskList.bind("<Button-1>", self.updateInfo)


        self.infoFrame = InfoFrame(self)
        self.infoFrame.grid(row=0, column=1)


        update_button = tk.Button(self, text="Update", command = self.updateInfo)
        update_button.grid(row = 1, column = 0)

    def save_all(self):
        for window in self.windows:
            window.save()

    def add_task(self):
        filename = tkFileDialog.askopenfilename()
        if filename is not None:
            self.windows.append(TileWindow(self, filename))

    def updateInfo(self):
        self.infoFrame.updateInfo()


class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)

        self.info_text = tk.StringVar()
        self.info_text.set("(Empty)")

        self.infoFrame = tk.Frame(self, height=50, width=50).grid(row=0, column=1)
        self.info_lable = tk.Label(self.infoFrame, textvariable=self.info_text, justify=tk.LEFT)
        self.info_lable.grid(row=0, column=1)


    def updateInfo(self):

        selectedTask = model['selected_task']
        if(selectedTask != None):
            self.info_text.set(
            "Name: {0}".format(model['selected_task'].name) +
                "\nDescription: {0}".format(model['selected_task'].description) +
                "\nStart Date: {0}".format(model['selected_task'].start_date) +
                "\nEnd Date: {0}".format(model['selected_task'].end_date) +
                "\nPath: {0}".format(model['selected_task'].path)          
            )

        else:
            self.info_text.set("(empty)")


class TaskList(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.list = tk.Listbox(self, selectmode=tk.SINGLE)
        self.list.grid(row = 0, column = 0)
        self.current = None
        self.poll()# start polling the list

        self.showTasks()

    def poll(self):
        now = self.list.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now

            if(len(now) > 0):
                selected_index = now[0]
                model['selected_task'] = model['tasks'][selected_index]
        
        self.after(250, self.poll)

    def list_has_changed(self, selection):
        print "selection is", selection

    def showTasks(self):
        self.list.delete(0, tk.END)

        for eachItem in model['tasks']:
            self.list.insert(tk.END, str(eachItem))
"""
class Taskbox(wx.HtmlListBox):
    def __init__(self, parent):
            wx.HtmlListBox.__init__(self, parent)
            self.data = [
                ("Foo", "3452-453"),
                ("Bar", "5672-346"),
            ]
            self.SetItemCount(len(self.data))

    def OnGetItem(self, n):
        return "<b>%s</b><br>%s" % self.data[n]

    def add_number(self, name, number):
        self.data.append((name, number))
        self.SetItemCount(len(self.data))
        self.Refresh()
"""

if __name__ == "__main__":
    app = MainView()
    app.mainloop()