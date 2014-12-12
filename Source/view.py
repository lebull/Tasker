import Tkinter as tk
import tkFont
import tkFileDialog

# --View Heiarchy--
#     TopView
#         MainView
#             InfoFrame
#             TaskList
#         AddView #Maybe this object should be named window?



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

        self.projectList = ProjectList(self)
        self.projectList.pack(side='left', fill='both', anchor='w', expand=1)

        self.infoFrame = InfoFrame(self)
        self.infoFrame.pack(side='right', fill='both', anchor='e', expand=1)

class ProjectList(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #Styling
        self.listFont = tkFont.Font(family="Helvetica", size=12)

        self.list = tk.Listbox(self, selectmode=tk.SINGLE, font=self.listFont)
        self.list.grid(row=0, column = 0)
        self.current = None

    def setProjects(self, data):
        self.list.delete(0, tk.END)

        for eachProject in data:
            self.list.insert(tk.END, str(eachProject.name))

class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)

        tk.Label(self, text="Name: ").grid(row=0, column=0, sticky='ne')        
        self.name = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.name.grid(row=0, column=1, sticky='nw' )

        tk.Label(self, text="Owner: ").grid(row=1, column=0, sticky='ne')       
        self.owner = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.owner.grid(row=1, column=1, sticky='nw')

        tk.Label(self, text="Edited Date: ").grid(row=2, column=0, sticky='ne')        
        self.updated_date = tk.Label(self, text="(empty)", justify=tk.LEFT)
        self.updated_date.grid(row=2, column=1, sticky='nw')

    def setInfo(self, inProject):
        self.name.config(text = str(inProject.name)        )
        self.owner.config(text = str(inProject.owner ) )
        self.updated_date.config(text = str(inProject.last_updated)  )

class AddProjectView(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.nameLabel = tk.Label(self, text="Name")
        self.nameLabel.pack()