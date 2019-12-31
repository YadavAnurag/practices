class Node:
	def __init__(self, data):
		self.data = data
		self.nextElement = None

class LinkedList:
	def __init__(self):
		self.headNode = Node(None)

	def getHead(self):
		return self.headNode

	def isEmpty(self):
		if self.headNode.nextElement == None:
			return True
		else:
			return False

	def printList(self):
		if self.headNode.nextElement == None:
			print('List is Empty')
			return False

		temp = self.headNode.nextElement
		while temp.nextElement != None:
			print(temp.data,' -> ',)
			temp = temp.nextElement
		print(temp.data,' -> ')

	def insertAtTail(self, dt):
		if self.isEmpty():
			self.insertAtHead(dt)
			return self.getHead()

		newNode = Node(dt)

		temp = self.getHead().nextElement
		while temp.nextElement != None:
			temp = temp.nextElement

		temp.nextElement = newNode
		newNode.nextElement = None 

		return self.getHead()


	def insertAtHead(self, dt):
		temp = Node(dt)
		temp.nextElement = self.headNode.nextElement
		self.headNode.nextElement = temp
		return self.getHead()



lst = LinkedList()
print(lst.isEmpty())

print(lst.getHead())

lst.printList()
for i in range(10):
	lst.insertAtTail(i)

lst.printList()

for i in range(10,20):
	lst.insertAtHead(i)

lst.printList()