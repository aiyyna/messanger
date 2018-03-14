#!/usr/bin/python3

from log_config import *
from user import *

class Chat():
	def __init__(self, chat_id, user_id):
		self.chat_id = chat_id
		self.list_users_id = [user_id]

	def add_user(self, user_id):
		self.list_users_id.append(user_id)

	def del_user(self, user_id):
		self.list_users_id.remove(user_id)
		
	def get_list_user_id(self):
		return self.list_users_id
		
	def spam_msg(self, msg, user_controller):
		list_users = self.list_users_id
		list_users.remove(msg.user_id)
		users = user_controller.users_in_list(list_users)
		for user in users:
			user.send_message(msg)


class Chat_Controller():
	def __init__(self):
		self.list_chats = {}

	def add_chat(self, chat):
		self.list_chats[chat.chat_id] = chat

	def get_chats(self, list_chats_id): #возвращает объекты по списку названий чатов
		list_chats_id = list(list_chats_id)
		chats = []
		for chat_id in list_chats_id:
			if chat_id in self.list_chats:
				chats.append(self.list_chats[chat_id])
		return chats
		
if __name__ == '__main__':
	control = Chat_Controller()
	chat1 = Chat('home', 'aina')
	control.add_chat(chat1)
	chat1.add_user('vlad')
	print(control.get_chats)
	print(chat1.get_list_user_id)
