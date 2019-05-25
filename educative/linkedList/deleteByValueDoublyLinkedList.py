

class Node:
	def __init__(self, data):
		self.data = data
		self.nextElement = None
		self.previousElement = None

class DoublyLinkedList:
	def __init__(self):
		self.headNode = Node(None)

	def getHead(self):
		return self.headNode

	def isEmpty(self):
		if self.getHead().nextElement == None:
			return True
		else:
			return False

	def printList(self):
		if self.isEmpty():
			print('List is Empty')
			return False

		temp = self.headNode.nextElement
		while temp.nextElement != None:
			print(temp.data,' -> ')
			temp = temp.nextElement
		print(temp.data,' -> None')
		return self.getHead()

	def insertAtHead(self, dt):
		newNode = Node(dt)
		newNode.nextElement = self.getHead().nextElement
		if not self.isEmpty():
			self.getHead().nextElement.previousElement = newNode
		self.getHead().nextElement = newNode
		newNode.previousElement = self.getHead()
		return self.getHead()

	def deleteByValue(self, value):
		if self.isEmpty():
			return False
		current = self.getHead()
		while current != None:
			if current.data == value:
				current.previousElement.nextElement = current.nextElement
				current.nextElement.previousElement = current.previousElement
				current = None 
				print(value,' deleted')
				return True
			current = current.nextElement
		return False







lst = DoublyLinkedList()
lst.printList()
for i in range(11):
	lst.insertAtHead(i)

lst.printList()

lst.deleteByValue(4)
lst.printList()