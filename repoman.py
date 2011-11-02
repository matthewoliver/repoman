#!/usr/bin/env python
"""Main API into the Kororaa Repomanagement system. 


"""
from log_manager import *
from config_manager import *

DEFAULT_ETC = "etc/repoman.conf"

class repoman():
	__server_manager=None
	__repo_manager=None
	__config_manager=None
	__repo_utils=None
	__log_manager=None
	
	def __init__(self, config_file = DEFAULT_ETC):
		try:
			self.__log_manager = log_manager(self)
			self.__config_manager = config_manager.config_manager(self, config_file)
			
			# Set the log file, if it is in the config file
			if self.__config_manager.hasConfigItem(CONFIG_LOG_FILE):
				self.__log_manager.setLogFile(self.__config_manager.getConfigItem(CONFIG_LOG_FILE))
			else:
				self.__log_manager.logWarning("No log file set, console logging only!")	
		except LogException as ex:
			#Log an warning as logging to screen will still take place.
			self.__log_manager.logWarning(str(ex))
		except ConfigException as ex:
			#Log an error
			self.__log_manager.logError(str(ex))

	def _getServerManager(self):
		return self.__server_manager

	def _getRepoManager(self):
		return self.__repo_manager

	def _getConfigManager(self):
		return self.__config_manager

	def _getLogManager(self):
		return self.__log_manager
			

def main():
	pass

if __name__ == "__main__":
	main()
