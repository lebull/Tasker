from task import *
import os
from os import path
import json
import copy

class Project:
    #Construct a project
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description
        self.tasks = []

    #TODO: Once again, pickle is a shitty way to save stuff.
    def saveProject(self, inPath):
        if os.access(os.path.dirname(inPath), os.W_OK):
            savefile = open(inPath, 'w')
            pickle.dump(self,savefile)
            savefile.close()
        else:
            raise RuntimeError("Cannot save in location: {0}".format(inPath))

    #And load stuff
    @staticmethod
    def loadProject(inPath):
        myFile = open(inPath, 'r')
        returnProject = pickle.load(myFile)
        myFile.close()

        return returnProject


    def __str__(self):
        returnString = ""
        returnString += "Name: {0}".format(self.name)
        returnString += "\nDescription: {0}".format(self.name)
        returnString += "\nTasks: {0}".format(len(self.tasks))

        return returnString




if __name__ == "__main__":
    myProject = Project(name = "Test", description = "Description")

    
    myProject.tasks.append(Task("New Task", "Description"))

    myProject.tasks.append(Task("Old Task", "Description"))
    myProject.tasks[-1].finish()

    myProject.tasks.append(Task("Bad Task", "FUCK"))

    myProject.tasks.append(Task("Good Task", "Description"))
    

    savePath = 'C:/Users/Tyler/Desktop/DevProjects/Tasker/Saves/Project_Save.pkl'
    myProject.saveProject(savePath)
    newProject = Project.loadProject(savePath)
    print myProject