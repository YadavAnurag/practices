class Node:
	def __init__(self, data):
		self.data = data
		self.nextElement = None

class LinkedList:
	def __init__(self):
		self.headNode = Node(None)

	def insertAtHead(self, dt):
		tempNode = Node(dt)
		tempNode.nextElement = self.headNode.nextElement
		self.headNode.nextElement= tempNode
		return self.headNode

	def isEmpty(self):
		if self.headNode.nextElement == None:
			return True
		else:
			return False

	def printList(self):
		if self.isEmpty():
			print('List is Empty')
			return False

		temp = self.headNode.nextElement
		while(temp.nextElement != None):
			print(temp.data,' -> ')
			temp = temp.nextElement
		print(temp.data,' -> ',None)

		return True

lst = LinkedList()
lst.printList()

for i in range(10):
	lst.insertAtHead(i)

lst.printList()



# def printList(self): 
# 	if(self.isEmpty()):
# 	  print "List is Empty"
# 	  return False   
# 	temp=self.headNode.nextElement     
# 	while(temp.nextElement!=None):
# 	 print temp.data , "->",
# 	 temp=temp.nextElement    
# 	print temp.data , "-> None"
# 	return True    
