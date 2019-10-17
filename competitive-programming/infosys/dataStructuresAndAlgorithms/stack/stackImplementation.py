class Stack:
	def __init__(self, maxSize):	
		self.__maxSize = maxSize
		self.__element = [None]*self.__maxSize
		self.__top = -1