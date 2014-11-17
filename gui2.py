"""
  TODO:
    -Pull in global model
    -Minimize to system tray 
      -http://www.blog.pythonlibrary.org/2013/07/12/wxpython-how-to-minimize-to-system-tray/

"""

#import ttk

import Tkinter as tk
import tkFileDialog

from taskerconfig import TaskerConfig
from task import *

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

class Model:
    def __init__(self):
        self.tasks = Observable(Task.getAllTasks())
        self.selectedTask = None

    #TODO:
    def addTask(self):
        pass


class MainView(tk.Toplevel):
    def __init__(self, master):

        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        ##---------- Menu Bar ----------##

        menubar = tk.Menu(self)
        self.configure(menu=menubar)

        fileMenu = tk.Menu(self)
        #fileMenu.add_command(label="New Task", command=self.add_task)

        menubar.add_cascade(label="Window", menu=fileMenu)

        ##---------- Main Layout ----------##

        self.taskList = TaskList(self)
        self.taskList.grid(row=0, column=0)

        self.infoFrame = InfoFrame(self)
        self.infoFrame.grid(row=0, column=1)

    """
    #What does this even do?
    def save_all(self):
        for window in self.windows:
            window.save()

    #TODO: We need to add a task file.
    def add_task(self):
        filename = tkFileDialog.askopenfilename()
        if filename is not None:
            self.windows.append(TileWindow(self, filename))
    """


class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)


        tk.Label(self, text="Name: ").grid(row=0, column=0)
        self.info_label = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.info_label.grid(row=0, column=1)


    def setInfo(self, value):
        self.info_label.delete(0,tk.END)
        self.info_label.insert(tk.END, str(value))


class TaskList(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.list = tk.Listbox(self, selectmode=tk.SINGLE)
        self.list.grid(row = 0, column = 0)
        self.current = None

        def setTasks(self, data):
            self.list.delete(0, tk.END)

            for eachItem in data:
                self.list.insert(tk.END, str(eachItem))

class Controller:
    def __init__(self, root):

        self.model = Model()
        self.mainView = MainView(root)

        self.model.tasks.addCallback(self.tasksChanged)
        self.tasksChanged()

        

    def tasksChanged(self):
        self.mainView.taskList.setTasks(self.model.tasks.get())

        """
        self.model = Model()
        self.model.myMoney.addCallback(self.MoneyChanged)
        self.view1 = View(root)
        self.view2 = ChangerWidget(self.view1)
        self.view2.addButton.config(command=self.AddMoney)
        self.view2.removeButton.config(command=self.RemoveMoney)
        self.MoneyChanged(self.model.myMoney.get())
        """
    """
    #Events for buttons and stuff
    def AddMoney(self):
        self.model.addMoney(10)

    def RemoveMoney(self):
        self.model.removeMoney(10)

    def MoneyChanged(self, money):
        self.view1.SetMoney(money)
    """



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = Controller(root)
    root.mainloop()