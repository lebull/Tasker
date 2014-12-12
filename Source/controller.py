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
        self.topView.fileMenu.add_command(label="New Project", command=self.launchAddProject)

        #Bind Model Values to View
        self.model.projects.addCallback(self.updateProjects)
        self.updateProjects(self.model.projects.get())

        self.model.selectedProject.addCallback(self.onSelectedProjectChanged)

        self.pollSelectedProject()


    def launchAddProject(self):
        self.addProjectView = AddProjectView(self.root)

    def updateProjects(self, inProjects):
        self.topView.mainView.projectList.setProjects(inProjects)

    #Polling method to get the selected task.
    def pollSelectedProject(self):

        pickedTasks = self.topView.mainView.projectList.list.curselection()
        if len(pickedTasks) > 0:
            selectedProject = pickedTasks[0]

            if selectedProject != self.model.selectedProject.get():
                self.model.selectedProject.set(selectedProject)
        
        self.topView.mainView.after(250, self.pollSelectedProject)

    def onSelectedProjectChanged(self, inProjectIndex):

        selectedProject = self.model.getProjectByIndex(inProjectIndex)
        self.topView.mainView.infoFrame.setInfo(selectedProject)