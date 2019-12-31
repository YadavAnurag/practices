class Node:
	def __init__(self, data):
		self.data = data
		self.nextElement = None

class LinkedList:
	def __init__(self):
		self.headNode = Node(None)

	def isEmpty(self):
		if self.headNode is None:
			return True
		return False

	def insertAtHead(self, data):
		newNode = Node(data)
		newNode = self.headNode.nextElement
		self.headNode.nextElement = newNode

	def insertAtTail(self, data):
		temp = self.headNode
		while temp.nextElement!=None:
			temp = temp.nextElement
		
		newNode = Node(data)
		temp.nextElement = newNode

	def printList(self):
		if self.isEmpty():
			print('List is Empty')
			return None
		temp = self.headNode
		while temp.nextElement!=None:
			temp = temp.nextElement
			print(temp.data)

	
def findNthFromEnd(n):
	mylist = LinkedList()
	mylist.insertAtHead(22)
	mylist.insertAtTail(18)
	mylist.insertAtTail(60)
	mylist.insertAtTail(47)
	mylist.insertAtTail(39)
	mylist.insertAtTail(99)

	main = mylist.headNode.nextElement
	ref = mylist.headNode.nextElement

	while n!=0:
		print(n)
		ref = ref.nextElement
		n -= 1

	while ref!= None:
		ref = ref.nextElement
		main = main.nextElement

	return main.data



l = LinkedList()

l.insertAtHead(22)
l.insertAtTail(18)
l.insertAtTail(60)
l.insertAtTail(7)
l.insertAtTail(47)
l.insertAtTail(39)
l.insertAtTail(99)

#l.printList()


n = int(input())

print(findNthFromEnd(n))




