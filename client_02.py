#!/usr/bin/python3

print ('Hello Aina')

import socket, json, time, sys
from message import *
from JIM import *
from chat import *

class Client():

	def __init__(self):
		#подсоединиться к серверу
		self.s = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
		self.s.connect(('localhost', 8888))
		# list_chats = self.server_get_chats(self.user_id)
		self.chat_controller = Chat_controller() # Chat_Controller(list_chats)

	def authorization(self, user_id, password):
		self.user_id = user_id
		self.password = password
		{
			"action": "authenticate",
			"time": time.ctime(time.time()) + "\n",
			"user": {
			"account_name": self.user_id,
			"password": self.password
			}
		}
		# send user_id and password to server for autenfication
		return self.user_id, self.password

	def process_msg(self, msg):
		if msg.msg_type is "usual":
			chat = self.chat_controller.get_chat(msg.chat_id)
			chat.send_msg(msg, self.s)

	def create_chat():
		#запрос на создание чата
		pass

	def join_chat():
		#добавитья в чат
		pass

	def quit_chat():
		#выйти из чата
		pass

class Interface():
	def get_msg(self):
		print("%s, you have the following contact list:" % self.name)
		print(self.list_contacts)

		try:
			self.current_chat
		except:
			if len(self.list_contacts) > 0:
				self.current_chat = self.list_contacts[0]
			else:
				self.current_chat = None

		input_chat = input("Type contact for chating (%s continue): " % self.current_chat)
		if input_chat != "":
			self.current_chat = input_chat
		# TODO: check that contact in list

		msg = input('write your message: ')
		chat_id = self.current_chat
		message = Message(self.name, chat_id, msg, "usual")
		return message

	def authorization(self):
		self.name = input('type your name: ')
		self.password = input('type your password: ')
		return self.name, self.password

client1 = Client()
console_interface = Interface()

user_id, password = console_interface.authorization()
log_in = client1.authorization(user_id, password)
print('='*10, 'авторизация прошла успешно!', '='*10)

console_interface.list_contacts = client1.chat_controller.get_chats_with_user(client1.user_id)

while True:
	message = console_interface.get_msg()
	print(message.__dict__)
	client1.process_msg(message)

# while True:
# 	jim = JIM_msg()
# 	msg = jim.create_message()
# 	msg = jim.encode_msg(msg)
# 	client1.send_msg(msg)
#ans = s.recv(1024)
#ans = (ans.decode())#json.loads(ans.decode())
#print(ans)
#result = json.dumps(result).encode() #перевести в джейсон 
#sock.send(result) #и отправить