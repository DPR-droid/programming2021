# lab10.2.timesheetentry.py
# Author David

class Timesheetentry:

    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration
    
    def __str__(self):
        return self.project + ':' + str(self.duration)