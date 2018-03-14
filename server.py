#!/usr/bin/python3

import socket, select
from log_config import *
from message import Message
from chat import *
import user


class Server():
	def __init__(self, address):
		sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
		sock.bind(address)
		sock.listen(5)
		sock.settimeout(0.2)
		self.socket_server = sock



# while True:
# 	user = User("Vlad")
# 	message = user.recv_message()
# 	if (message is not None):
# 		print(message.__dict__)
# 	else:
# 		print("We don't have message")