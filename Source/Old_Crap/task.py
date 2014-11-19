#https://docs.python.org/2/library/datetime.html
from datetime import datetime as DateTime
import pickle
import json
import os.path

from taskfilemanager import *



class Task:
	name = 'Empty'
	description = 'Empty'
	complete = False
	start_date = DateTime.today()
	end_date = None
	todo_list = []

	path = ""
	file_list = None


	def __init__(self, name ="", description = "", start_date = DateTime.today()):

		self.name = name
		self.description = description
		self.start_date = start_date

	def __str__(self):
		returnString = self.name

		return returnString

	def setPath(self, inPath):
		self.path = inPath.replace('\\', '/')
		print self.path + '\n'
		self.getFiles()

	def getFiles(self):
		(directories, files) = TaskFileManager.getFilesFromPath(self.path)
		self.file_list = files + directories


	@staticmethod
	def createTask(inPath, name = "", description = "", start_date = DateTime.today()):
		newTask = Task(name, description, start_date)
		newTask.setPath(inPath)
		Task.encode(newTask)
		return Task

	#TODO
	@staticmethod
	def deleteTask():
		pass

	#TODO: Pickle is in no way the best way to keep these tasks.
	@staticmethod
	def encode(inTask):

		savefile = open(inTask.path + "/" + TaskerConfig.tasker_filename, 'w')
		pickle.dump(inTask,savefile)
		savefile.close()

	@staticmethod
	def decode(inFile):
		myFile = open(inFile, 'r')
		returnTask = pickle.load(myFile)
		myFile.close()

		inPath = os.path.dirname(inFile)

		#If the task was moved, we need to reset the task's stored path.
		if(inPath != returnTask.path):
			returnTask.setPath(inPath)
			#Task.encode(returnTask)

		return returnTask

	@staticmethod
	def getAllTasks():

		taskList = []
		for eachFile in TaskFileManager.getAllTaskFiles():
			taskList.append(Task.decode(eachFile))

		return taskList	


class TaskTodoItem:
	name = 'Empty'
	description = 'Empty'
	complete = False
	start_date = DateTime.today()
	end_date = None

	def __init__(self, name, description = "", start_date = DateTime.today()):
		
		self.name = name
		self.description = description
		self.start_date = start_date

	def __str__(self):
		returnString = "--Todo--\n"
		returnString += " {0}: {1}\n".format(self.name, self.complete)
		returnString += "\tDescription: {0}\n".format(self.description)
		returnString += "\tStart Date: {0}\n".format(self.start_date)
		returnString += "\tEnd Date: {0}\n".format(self.end_date)
		return returnString

	def finish():
		self.complete = True
		self.end_date = DateTime.today()




