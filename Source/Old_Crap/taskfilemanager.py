#https://docs.python.org/2/library/os.html
from os import walk
from taskerconfig import TaskerConfig

#TODO: We don't need all this unknown/known directories.

class TaskFileManager:

	unknownDirectories = []
	knownProjects = []

	@classmethod
	def getFilesFromPath(cls, path):
		#http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
		outfiles = []
		outdirs = []

		for (dirpath, dirnames, filenames) in walk(path):
			for file_ in filenames:
				if(not file_.startswith('~')):
					outfiles.append(file_)

			outdirs.extend(dirnames)
			break

		return (outdirs, outfiles)

	## Search through the inputted path and look for directories
	## that may contain a project.
	@classmethod
	def getUnknownDirectories(cls, path):
		found_files = cls.getFilesFromPath(path)[0]
		cls.unknownDirectories.extend(found_files)
		return found_files

	## Attempt to find and return a task file from a given path.
	@classmethod
	def getTaskFromPath(cls, path):

		#TODO: Check if it's even a freeking valid path.

		(directories, files) = cls.getFilesFromPath(path)

		try:
			fileIndex = files.index(TaskerConfig.tasker_filename)
		except ValueError:
			return None

		return path + "/" + files[fileIndex]

	@classmethod
	def getAllTaskFiles(cls):

		cls.getUnknownDirectories(TaskerConfig.tasker_directory)

		returnPaths = []

		for directory in cls.unknownDirectories:

			path = TaskerConfig.tasker_directory + directory
			taskPath = TaskFileManager.getTaskFromPath(path)
			if(taskPath != None):

				returnPaths.append(taskPath)

		return returnPaths




	#TODO: Process unknown directories to populate tasks.
