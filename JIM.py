import socket, json

class JIM_msg:
	sms = input('write your message or "q" for exit')
			if sms == 'presence':
				sms = {
				"action": "presence",
				"time": time.ctime(time.time()) + "\n",
				"type": "status",
				"user": {
				"account_name": "C0deMaver1ck",
				"status": "Yep, I am here!"
				}
				}
			elif sms == 'q':
				sms = {
				"action": "quit",
				"time": time.ctime(time.time()) + "\n",
				}
				print('Good bye')

			else:
				sms = {
				"action": "msg",
				"time": time.ctime(time.time()) + "\n",
				"to": "status",
				"from": "account_name"
				"encoding": "ascii",
				"message": sms
				}

class JIM_res:
	pass
