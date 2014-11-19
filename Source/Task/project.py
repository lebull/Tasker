from task import *

class Project:
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description
        self.tasks = []

    def saveProject(self, inPath):
        savefile = open(inPath, 'w')
        pickle.dump(inTask,savefile)
        savefile.close()

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
    print myProject