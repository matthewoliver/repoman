"""This file is to be used as a place to put useful methods, think of it as a common library.
"""
import datetime


def getTimeStamp(date = datetime.datetime.now()):
	return date.isoformat()
