print ('Hello Aina')


import socket, json, time, sys

class Client():

	def __init__(self):
		#подсоединиться к серверу
		self.s = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
		self.s.connect(('localhost', 8888))
		# list_chats = self.server_get_chats(self.user_id)
		self.chat_controller = Chat_Controller() # Chat_Controller(list_chats)

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

class Chat_Controller():

	def get_chat(self, chat_id):
		chat = Chat() # TMP!!!
		return chat

	def get_list_chats(self):
		list_chats = ['aina', 'vlad', 'kulikov']
		return list_chats

class JIM_msg():

	def create_message(self):
		sms = input('write your message or "q" for exit\n')
		if sms == 'presence':
			sms = {
				"action": "presence",
				"time": time.ctime(time.time()) + "\n",
				"type": "status",
				"user": {
					"account_name": self.user_id,
					"status": "Yep, I am here!"
				}
			}
		elif sms == 'q':
			sms = {
				"action": "quit",
				"time": time.ctime(time.time()) + "\n",
			}
			sys.exit()
			print('Good bye')
		else:
			to = input('Кому вы хотите послать сообщение? ')
			sms = {
				"action": "msg",
				"time": time.ctime(time.time()) + "\n",
				"to": to,
				"from": self.user_id,
				"encoding": "ascii",
				"message": sms
			}
		print('='*20, 'Сообщение сформировано', '='*20)
		return sms

	def encode_msg(self, msg):
		
		sms = json.dumps(msg).encode()
		return sms

	def decode_msg(self, msg):
		sms = json.loads(msg.decode())
		return sms

	def create_message(self):
		sms = input('write your message or "q" for exit\n')
		if sms == 'presence':
			sms = {
				"action": "presence",
				"time": time.ctime(time.time()) + "\n",
				"type": "status",
				"user": {
					"account_name": self.user_id,
					"status": "Yep, I am here!"
				}
			}
		elif sms == 'q':
			sms = {
				"action": "quit",
				"time": time.ctime(time.time()) + "\n",
			}
			sys.exit()
			print('Good bye')
		else:
			to = input('Кому вы хотите послать сообщение? ')
			sms = {
				"action": "msg",
				"time": time.ctime(time.time()) + "\n",
				"to": to,
				"from": self.user_id,
				"encoding": "ascii",
				"message": sms       
			}
		print('='*20, 'Сообщение сформировано', '='*20)
		return sms

class Chat():
	def send_msg(self, sms, socket):
		jim_msg = JIM_msg()
		sms = jim_msg.encode_msg(sms.__dict__)
		socket.send(sms)
		print('='*20, 'Сообщение отправлено', '='*20)

	def recv_msg(self, sms, socket):
		sms = self.s.recv(1024)
		logging.info('Сообщение принято')
		print(sms)

class Interface():
	def get_msg(self):
		print("%s, you have the following contact list:" % self.name)
		print(self.list_contacts)

		try:
			self.current_chat
		except:
			self.current_chat = self.list_contacts[0]
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


class Message():
	def __init__(self, userID, chatID, string, type_msg):
		self.user_id = userID
		self.chat_id = chatID
		self.msg_str = string
		self.msg_type = type_msg



client1 = Client()
console_interface = Interface()

console_interface.list_contacts = client1.chat_controller.get_list_chats()


user_id, password = console_interface.authorization()
log_in = client1.authorization(user_id, password)
print('='*10, 'авторизация прошла успешно!', '='*10)

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



