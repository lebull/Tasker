from Task import *

from model import *
from view import *


class Controller:
    def __init__(self, root):

        #Initialize Model
        self.model = Model()

        #Initialize View
        self.root = root
        self.topView = TopView(root)

        #Create Menues
        self.topView.fileMenu.add_command(label="New Task", command=self.launchAddTask)

        #Bind Model Values to View
        self.model.tasks.addCallback(self.updateTasks)
        self.updateTasks(self.model.tasks.get())

        self.model.selectedTask.addCallback(self.onSelectedTaskChanged)
        self.pollSelectedTask()

        #Testing
        #self.launchAddTask()

    def launchAddTask(self):
        self.addView = AddView(self.root)

    def updateTasks(self, inTasks):
        self.topView.mainView.taskList.setTasks(inTasks)

    #Polling method to get the selected task.
    def pollSelectedTask(self):

        pickedTasks = self.topView.mainView.taskList.list.curselection()
        if len(pickedTasks) > 0:
            selectedTask = pickedTasks[0]

            if selectedTask != self.model.selectedTask.get():
                self.model.selectedTask.set(selectedTask)
        
        self.topView.mainView.after(250, self.pollSelectedTask)

    def onSelectedTaskChanged(self, inTaskIndex):

        selectedTask = self.model.getTaskByIndex(inTaskIndex)
        self.topView.mainView.infoFrame.setInfo(selectedTask)