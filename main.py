#Browsing files
from taskerconfig import TaskerConfig
from task import *

model = {}
model['tasks'] = Task.getAllTasks()
model['selected_task'] = None


