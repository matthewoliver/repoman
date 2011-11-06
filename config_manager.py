import ConfigParser

#KEY CONSTANTS
CONFIG_LOG_FILE = "log_file"
CONFIG_REPO_PATH = "repo_path"
CONFIG_WORKING_PATH = "working_path"
CONFIG_CACHE_PATH = "cache_path"
CONFIG_SERVER_URL = "server_url" 

DEFAULT_SECTION = "main"

DEFAULT_VALUES = {
	CONFIG_LOG_FILE : "/var/log/repoman.log",
	CONFIG_REPO_PATH : "/etc/yum.repos.d/",
	CONFIG_WORKING_PATH : "var/cache/repoman/working",
	CONFIG_CACHE_PATH :. "var/cache/repoman/",
	CONFIG_SERVER_URL : "http://oliver.net.au/repos/",
}

class config_manager():
	__config_items=None	
	__config_file=None
	__repoman=None

	def __init__(self, repoman, config_file):
		self.__repoman = repoman
		self.__config_items=[]
		self.__config_file=config_file
		
		parseConfig()

	
	def parseConfig(self):
		config = ConfigParser.ConfigParser(DEFAULT_VALUES)
		config.read(__config_file)
		
		self.__config_items[CONFIG_LOG_FILE] = config.get(DEFAULT_SECTION, CONFIG_LOG_FILE)
		self.__config_items[CONFIG_REPO_PATH] = config.get(DEFAULT_SECTION, CONFIG_REPO_PATH)
		self.__config_items[CONFIG_WORKING_PATH] = config.get(DEFAULT_SECTION, CONFIG_WORKING_PATH)
		self.__config_items[CONFIG_CACHE_PATH] = config.get(DEFAULT_SECTION, CONFIG_CACHE_PATH)
		self.__config_items[CONFIG_SERVER_URL] = config.get(DEFAULT_SECTION, CONFIG_SERVER_URL)
		

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
