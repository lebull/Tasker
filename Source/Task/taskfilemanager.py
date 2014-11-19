#https://docs.python.org/2/library/os.html
from os import walk
from task import *

#TODO: We don't need all this unknown/known directories.

class TaskFileManager:

	@staticmethod
	def LoadTasksFromFile(inFile = ""):

		cls.getUnknownDirectories(TaskerConfig.tasker_directory)

		returnPaths = []

		for directory in cls.unknownDirectories:

			path = TaskerConfig.tasker_directory + directory
			taskPath = TaskFileManager.getTaskFromPath(path)
			if(taskPath != None):

				returnPaths.append(taskPath)

		return returnPaths




	#TODO: Process unknown directories to populate tasks.
