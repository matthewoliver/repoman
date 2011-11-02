#KEY CONSTANTS
CONFIG_LOG_FILE = "log_file"
CONFIG_REPO_PATH = "repo_path"
CONFIG_WORKING_PATH = "working_path"
CONFIG_CACHE_PATH = "cache_path"
CONFIG_SERVER_URL = "server_url" 

class config_manager():
	__config_items=None	
	__config_file=None
	__repoman=None

	def __init__(self, repoman, config_file):
		self.__repoman = repoman
		self.__config_items=[]
		self.__config_file=config_file

	
	def hasConfigItem(self, key):
		return self.__config_items.__contains__(key)

	def getConfigItem(self, key):
		if self.hasConfigItem(key):
			return __config_items[key]
		else:
			return None


class ConfigException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
