import time, json

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