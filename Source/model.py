from pytodoist import todoist

#http://pytodoist.readthedocs.org/en/latest/modules.html#pytodoist.todoist.Project
#import Task

#A class that holds any data, but will execute callbacks if the data is set.

class Model:
    def __init__(self):

        self.selectedProject = Observable(None)
        self._api_token = 'c37ac7d6aaf139372705b239f73855c29728e088'
        self._user = todoist.login_with_api_token(self._api_token)

        self.projects = Observable([])

        self.releventProjects = Observable([])
        
        self.refreshData()

    def refreshData(self):
        self.projects.set(self._user.get_projects())

    #I DON'T THINK THIS IS A GOOD IDEA
    def getProjectByIndex(self, index):
        project = self.projects.get()[index]
        return project

    #Return all projects that fall under a single parent project.
    def getAllChildProjects(self, parentProjectName):

        returnProjects = []

        allProjects = self._user.get_projects()

        try:
            rootProjectIndex = self._user.get_project(parentProjectName).item_order
        except AttributeError:
            raise AttributeError("Parameter '{}' is not a project name.".format(parentProjectName))
            return []


        #Find the projects that fall under Work.
        for project in allProjects[rootProjectIndex + 1:]:

            if(project.indent == 1):
                break

            returnProjects.append(project)
            #print "\t" * project.indent + "Name: {}\tOrder: {}".format(project.name, project.item_order)

        return returnProjects

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

    childProjects = model.getAllChildProjects('Work')

    for project in childProjects:
        project_indent = project.indent - 1
        print "\t" * project_indent + "Project: {}".format(project.name)
        for task in project.get_tasks():
            task_indent = task.indent
            print "\t" * project_indent + "\t" * task.indent + "Task: {}".format(task.content)