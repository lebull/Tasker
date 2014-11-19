#https://docs.python.org/2/library/datetime.html
from datetime import datetime as DateTime
import pickle

class Task:
    name = 'Empty'
    description = 'Empty'
    complete = False
    start_date = DateTime.today()
    end_date = None


    def __init__(self, name ="", description = "", start_date = DateTime.today()):
        self.name = name
        self.description = description
        self.startDate = start_date
        self.finishedDate = None
        self.finished = False

    def finish(self, finishedDate = DateTime.today()):
        self.finished = True
        self.finishedDate = self.finishedDate

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

