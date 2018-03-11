import logging

import logging.handlers
def log_init():
	log_format = '%(asctime)s :%(levelname)s : %(module)s : %(funcName)s :%(message)s'
	logging.basicConfig(
		filename='logging_file', 
		level=logging.DEBUG,
		filemode = 'w',
		format = log_format,
	)


	logging.getLogger().addHandler(logging.StreamHandler())
	logger = logging.getLogger()
	
#	handler = logging.StreamHandler()
#	formatter = logging.Formatter(log_format)
#	handler.setFormatter(formatter)
#	logger.addHandler(handler)

