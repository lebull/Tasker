from Task import *

#A class that holds any data, but will execute callbacks if the data is set.

class Model:
    def __init__(self):

        myProject = Project.loadProject('C:/Users/Tyler/Desktop/DevProjects/Tasker/Saves/Project_Save.pkl')
        
        self.project = Observable(myProject)
        taskList = self.project.get().tasks
        self.tasks = Observable(taskList)

        self.selectedTask = Observable(None)

    def getTaskByIndex(self, inIndex):
        taskList = self.tasks.get()
        return taskList[inIndex]
    #TODO:
    def addTask(self):
        pass


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

if __name__ == '__main__':
    model = Model()