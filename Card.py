class Card():
	def __init__(self, suit, type):
		self.__suit = suit
		self.__type = type

	def get_suit(self):
		return self.__suit

	def get_type(self):
		return self.__type