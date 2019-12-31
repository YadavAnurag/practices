class Node:
	def __init__(self, data):
		self.data = data
		self.nextElement = None

class LinkedList:
	def __init__(self):
		self.headNode = Node(None)

	def isEmpty(self):
		if self.headNode.nextElement == None:
			return True
		else:
			return False

	def getHead(self):
		return self.headNode

	def printList(self):
		if self.isEmpty():
			print('List is Empty')
			return False

		temp = self.headNode.nextElement
		while temp.nextElement != None:
			print(temp.data,' -> ')
			temp = temp.nextElement
		print(temp.data,' -> None')

	def insertAtHead(self, dt):
		newNode = Node(dt)
		newNode.nextElement = self.getHead().nextElement
		self.getHead().nextElement = newNode
		return self.getHead()

	def insertAtTail(self, dt):
		newNode = Node(dt)
		if self.isEmpty():
			self.insertAtHead(dt)
			return self.getHead()

		temp = self.getHead()
		while temp.nextElement != None:
			temp = temp.nextElement
		
		temp.nextElement = newNode
		return self.getHead()

	def insertAtNth(self, dt, pos):
		count = 0
		newNode = Node(dt)
		current = self.getHead()
		prev = None

		if pos == 0:
			self.insertAtHead(dt)
			return self.getHead()

		while count<pos:
			prev = current
			current = current.nextElement
			count += 1

		newNode.nextElement = prev.nextElement
		prev.nextElement = newNode
		return self.getHead()

	def deleteAtHead(self):
		if self.isEmpty():
			return False
		first = self.getHead().nextElement
		self.getHead().nextElement = first.nextElement
		first = None
		return self.getHead()

	def deleteByValue(self, value):
		if self.isEmpty():
			return False
		prev = self.getHead()
		current = prev.nextElement
		while current!=None:
			if current.data == value:
				prev.nextElement = current.nextElement
				current = None 
			prev = prev.nextElement
			current = prev.nextElement
		return self.getHead()

	def deleteAtTail(self):
		if self.isEmpty():
			return False
		prev = self.getHead()
		current = self.getHead().nextElement
		while current.nextElement!=None:
			prev = prev.nextElement
			current = current.nextElement
		prev.nextElement = None 
		current = None 
		return self.getHead()

	def reverse(self): 
		previous = None
		current = self.getHead().nextElement
		later = None 
		while current != None:
			later = current.nextElement
			current.nextElement = previous
			previous = current 
			current = later
		self.headNode.nextElement = previous
		return self.getHead() 


lst = LinkedList()
lst.printList()
for i in range(5):
	lst.insertAtTail(i)
lst.printList()

a = lst.reverse()
print('reverse')
# print(a.data)
lst.printList()



