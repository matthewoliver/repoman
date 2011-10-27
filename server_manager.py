class server_manager():
	__connected=None	

	def __init__(self):
		__connected=False

	
	def isConnected(self):
		return self.__connected
