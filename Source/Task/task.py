#https://docs.python.org/2/library/datetime.html
from datetime import datetime as DateTime
import pickle

class Task:
    name = 'Empty'
    description = 'Empty'
    complete = False
    start_date = DateTime.today()
    end_date = None
    childTasks = []


    def __init__(self, name ="", description = "", start_date = DateTime.today()):
        self.name = name
        self.description = description
        self.startDate = start_date
        self.finishedDate = None
        self.finished = False

    def finish(self, finishedDate = DateTime.today()):
        self.finished = True
        self.finishedDate = self.finishedDate

    #save it...
    def addChildTask(self, inTask):
        self.childTasks.append(inTask)

    #When saving this, we need to encode it since this is a specific class.
    def encode(self):
        return pickle.dumps(self)

    #And decode it when we need it.
    @staticmethod
    def decode(inData):
        return pickle.loads(self)

    def __str__(self):
        returnString = self.name
        return returnString


#Blah, save it for later.  It could be cool
class TaskTree:

    def __init__(self):
        self.root = None
        self.pointer = self.root




