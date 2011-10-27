class config_manager():
	__config_items=None	

	def __init__(self):
		__config_items=[]

	
	def hasConfigItem(self, key):
		return self.__config_items.has_key(key)
