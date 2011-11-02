import utils

SEVERITY_FINE = 1
SEVERITY_WARNING = 2 
SEVERITY_ERROR = 3 

STR_SEVERITY = {
	SEVERITY_FINE : "FINE"
	SEVERITY_WARNING : "WARNING"
	SEVERITY_ERROR : "ERROR"
}

LOG_TEMPLATE = "%s %s: %s\n"

class log_manager():
	__logfile=None	
	__repoman=None

	def __init__(self, repoman):
		self.__repoman=repoman

	def setLogFile(self, logfile):
		self.__logfile = logfile
	
	def log(self, severity, message):
		msg = LOG_TEMPLATE % (utils.getTimeStamp(),  STR_SEVERITY[severity], message)
		
		#If the log file is set log to the file. 
		if self.__logfile != None:
			# Log to file
		
		# Log to the console as well
		print msg
	
	def logFine(self, message):
		self.log(SEVERITY_FINE, message)

	def logWarning(self, message):
		self.log(SEVERITY_WARNING, message)

	def logError(self, message):
		self.log(SEVERITY_ERROR, message)


class LogException(Exception):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
