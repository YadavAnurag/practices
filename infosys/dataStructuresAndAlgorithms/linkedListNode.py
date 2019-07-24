class Node:
	def __init__(self, data):
		self.__data = data
		self.__next = None

	def getData(self):
		return self.__data

	def setData(self, value):
		self.__data = value

	def getNext(self):
		return self.__next

	def setNext(self, nextNode):
		self.__next = nextNode

itemNode = Node('Laptop')
print(itemNode.getData())
