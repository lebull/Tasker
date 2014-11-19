"""
  TODO:
    View:
        -Add Task
        -Task Details
        -Minimize to system tray 
        -Maybe a more flexible view system? (Be able to exchange views)
    -Task:
        -Consider saving as multiple file types
        -Todo/subtask

      -http://www.blog.pythonlibrary.org/2013/07/12/wxpython-how-to-minimize-to-system-tray/
"""
#import ttk

from Task import *

from controller import *


import Tkinter as tk

if __name__ == '__main__':
    #Spawn the main app
    root = tk.Tk()

    #And get rid of it... we're using our own :3
    root.withdraw()

    #Spawn our controller
    app = Controller(root)
    
    root.mainloop()