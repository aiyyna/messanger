class Message():
	def __init__(self, userID, chatID, string, type_msg):
		self.user_id = userID
		self.chat_id = chatID
		self.msg_str = string
		self.msg_type = type_msg
