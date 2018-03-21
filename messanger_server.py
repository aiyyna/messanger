#!/usr/bin/python3

from server import *
from log_config import *

logger.info("Start work")

server = Server('localhost', 8888)
logger.info("Created socket. Listening...")

while True:
	server.check_new_clients()
	server.check_online_clients()
	print(server)

