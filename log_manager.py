SEVERITY_FINE=0

class log_manager():
	__logfile=None	
	__repoman=None

	def __init__(self, repoman):
		self.__repoman=repoman

	
	def log(self, severity, message):
		pass
	
	def logFine(self, message):
		self.log(SEVERITY_FINE, message)
