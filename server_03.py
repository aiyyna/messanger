import json, socket, select, time
from log_config import *
print('Hello, Aina!')

class Server():
	def new_client(self, address):
		sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
		sock.bind(address)
		sock.listen(5)
		sock.settimeout(0.2)
		return sock

class JIM_recv():
	def create_message(self):
		pass

	def encode_msg(self, msg):
		sms = json.dumps(msg).encode()
		return sms

	def decode_msg(self, msg):
		sms = json.loads(msg.decode())
		return sms

class Chat_controller():
	#
	pass

class Chat():
	def send_msg(self, sms, socket):
		jim_msg = JIM_recv()
		sms = jim_msg.encode_msg(sms.__dict__)
		socket.send(sms)

	def recv_msg(self, sms, socket):
		sms = self.s.recv(1024)
		logging.info('Сообщение принято')
		print(sms)
	pass

class User_controller():
	#
	pass

class User():
	def autentification(self):
		pass

while True:
	server = Server()