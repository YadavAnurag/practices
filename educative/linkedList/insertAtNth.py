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


	def removeDuplicates(self):
		currentNode = self.getHead().nextElement
		prevNode = self.getHead()

		visitedNodes = set()
		if(not self.isEmpty() and currentNode.nextElement !=None):
			while(currentNode != None):
				value = currentNode.data
				if (value in visitedNodes):
					prevNode.nextElement = currentNode.nextElement
					currentNode = currentNode.nextElement
					continue
				visitedNodes.add(currentNode.data)
				prevNode = currentNode
				currentNode = currentNode.nextElement
		return self.getHead()



	def intersection(self,list1,list2):
  		mylist = LinkedList()
  		myset = set()
  		list2.removeDuplicates()
  		temp1 = list1.getHead().nextElement
  		myset.add(temp1.data)
  		while temp1!= None:
  			myset.add(temp1.data)
  			temp1 = temp1.nextElement
  		count = len(myset)
  		temp2 = list2.getHead().nextElement
  		while temp2.nextElement != None:
  			if temp2.data in myset:
  				mylist.insertAtTail(temp2.data)
  			temp2 = temp2.nextElement
  		return mylist







# lst1 = LinkedList()
# lst2 = LinkedList()
# print('List1')
# lst1.printList()
# print('List2')
# lst2.printList()



# lst1.insertAtTail(10)
# lst1.insertAtTail(20)
# lst1.insertAtTail(80)
# lst1.insertAtTail(80)
# lst1.insertAtTail(60)

# lst2.insertAtTail(15)
# lst2.insertAtTail(20)
# lst2.insertAtTail(30)
# lst2.insertAtTail(60)
# lst2.insertAtTail(45)
# lst2.insertAtTail(45)


# print('List1')
# lst1.printList()
# print('List2')
# lst2.printList()



# lst1.intersection(lst1,lst2)
