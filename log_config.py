#!/usr/bin/python3

import logging

def log_init():
	log_format = '%(asctime)s :%(levelname)s : %(module)s : %(funcName)s :%(message)s'

	logFormatter = logging.Formatter(log_format)
	my_logger = logging.getLogger()

	fileHandler = logging.FileHandler("messanger_server.log")
	fileHandler.setFormatter(logFormatter)
	my_logger.addHandler(fileHandler)

	consoleHandler = logging.StreamHandler()
	consoleHandler.setFormatter(logFormatter)
	my_logger.addHandler(consoleHandler)

	my_logger.setLevel(logging.DEBUG)

	logger = my_logger

	return my_logger

logger = log_init()

if __name__ == '__main__':
	logger = log_init()

	logger.debug('debug message')
	logger.info('info message')
	logger.warn('warn message')
	logger.error('error message')
	logger.critical('critical message')
