#!/usr/bin/python3
import socket
from JIM import *

class User():
	def __init__(self, socket, user_id):
		self.socket = socket
		self.user_id = user_id
		self.status = True

	def __repr__(self):
		if self.status == True:
			status_str = "online"
		else:
			status_str = "offline"
		return 'This is objects %s with status %s\n' % (self.user_id, status_str)
		


	def send_message(self, message):
		jim_msg = JIM_msg()
		msg = encode.jim_msg(msg.__dict__)
		socket.send(msg)

	def recv_message(self):
		rand = random.randint(1, 10)
		if (rand == 4):
			message =  Message(self.user_id, "general", "Test message", "usual") 
			#print(message.__dict__)
			return message

	def set_status_on(self, socket):
		self.status = True
		self.socket = socket
		
	def set_status_off(self):
		self.status = False
		# self.socket.close()

	def is_online(self):
		return True 

class User_controller():
	def __init__(self):
		self.list_users = {}

	def add_user(self, user):
		self.list_users[user.user_id] = user

	def  users_is_on(self):
		users = []
		for key in self.list_users.keys():
			user = self.list_users[key]
			if user.status == True:
				users.append(user)
		return users

	def users_in_list(self, list_user_ids):
		users = []
		list_user_ids = list(list_user_ids)
		for user_id in list_user_ids:
			if user_id in self.list_users.keys():
				users.append(self.list_users[user_id])
		return users

if __name__ == '__main__':

	user1 = User(None, 'Aina')
	user2 = User(None, 'Vlad')
	user3 = User(None, 'Gleb')
	user4 = User(None, 'Ignat')
	user5 = User(None, 'Vladik')

	user2.set_status_off()
	user5.set_status_off()

	control = User_controller()

	control.add_user(user1)
	control.add_user(user2)
	control.add_user(user3)
	control.add_user(user4) 
	control.add_user(user5)

	print(control.users_is_on())

	user2.set_status_on(None)
	print(control.users_is_on())
 
	print(control.users_in_list(['Vladik', 'Ignat']))
