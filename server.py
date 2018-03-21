#!/usr/bin/python3

import socket, select
from log_config import *
from message import Message
from chat import *
import user


class Server():
	def __init__(self, host, port):
		sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
		sock.bind((host, port))
		sock.listen(5)
		sock.settimeout(0.2)
		self.socket_server = sock
		self.chat_controller = Chat_controller()
		self.user_controller = User_controller()
		self.authorize_controller = User_controller()
		self.tmp_id = 0

	def check_new_clients(self):
		try:
			new_socket, client_address = self.socket_server.accept()
		except OSError as e:
			pass
		else:
			logger.info('Получен запрос на соединение от %s' % str(client_address))
			tmp_user = User(new_socket, 'tmp_user_%s' % self.tmp_id)
			self.tmp_id += 1
			self.authorize_controller.add_user(tmp_user)

	#def check_authorize_msg(self):


	def __repr__(self):
		return "server has %s clients for authorize and %s clients online " % (self.authorize_controller.get_number_users(), self.user_controller.get_number_users())

	def check_online_clients(self):
		list_users_online = self.user_controller.users_is_on() + self.authorize_controller.users_is_on() 

		for user in list_users_online:
			r_sock, w_sock, e_sock = select.select([user.user_socket()], [], [])
			if len(e_sock) != 0:
				user.set_status_off()


	# def mainloop(self):
	# 	address = (host, port)
	# 	s = self.check_new_clients(address)
		
	# 	while True:
	# 		try:
	# 			conn, addr = s.accept()
	# 		except OSError as e:
	# 				pass
	# 		else:
	# 			logging.info('Получен запрос на соединение от %s' % str(addr))
	# 			print('connected')
	# 			clients.append(conn)
	# 		finally:
	# 			w_sock = []
	# 			r_sock = []
	# 			r_sock, w_sock, e_sock = select.select(clients, clients, [], 0)
	# 			for s_client in e_sock:
	# 				self.close_client(clients)
		
	# 				print('что-то случилось')	
	# 			for s_client in w_sock:
	# 				timestr = time.ctime(time.time()) + "\n"
	# 				try:
	# 					s_client.send(timestr.encode('ascii'))
	# 				except:
	# 					self.close_client(s_client, clients)
		
	# 			for s_client in r_sock:
	# 				try:
	# 					msg = s_client.recv(1024)
	# 					sms = json.loads(msg.decode())
	# 					logging.info('Message receive')
	# 					print('Сообщение: ', sms)
	# 				except:
	# 					self.close_client(s_client, clients)