# directed graph
class myQueue:
	def __init__(self, num=None):
		self.queueList = []

	def isEmpty(self):
		return len(self.queueList) == 0

	def front(self):
		if self.isEmpty():
			return None
		return self.queueList[0]

	def back(self):
		if self.isEmpty():
			return None
		return self.queueList[-1]

	def size(self):
		return len(self.queueList)

	def enqueue(self, value):
		self.queueList.append(value)

	def dequeue(self):
		if self.isEmpty():
			return None
		return self.queueList.pop(0)



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




class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.array = []

		for i in range(vertices):
			temp = LinkedList()
			self.array.append(temp)

	def addEdge(self, source, destination):
		self.array[source].insertAtHead(destination)
		#If we were to implement an Undirected Graph i.e (1,0) == (0,1) 
	    #We would create an edge from destination towards source as well
	    #i.e self.list[destination].insertAtHead(source) 


	def printGraph(self):
		print('Adjacency List of Directed Graph\n')
		for i in range(self.vertices):
			print('Node ',i, ' => ')
			temp = self.array[i].getHead().nextElement
			while temp!= None:
				print(' -> ',temp.data)
				temp = temp.nextElement
			print(' -> None')

def bfsTraversal(g, source):
	result = ''

	numOfVertices = g.vertices 
	queue = myQueue()
	result += str(source)
	queue.enqueue(source)
	while not queue.isEmpty():
		v = queue.dequeue()
		temp = g.array[v].getHead().nextElement
		while temp != None:
			if str(temp.data) not in result:
				result += str(temp.data)
				queue.enqueue(temp.data)
			temp = temp.nextElement
	return result


result = ""
def dfsRecursive(g, source):
	global result
	visited = []
	visited.append(source)
	result += str(source)
	print(source)
	temp = g.array[source].getHead().nextElement
	while temp != None:
		if temp.data not in visited:
			dfsRecursive(g, temp.data)
		temp = temp.nextElement
	return result



g = Graph(6)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)

g.printGraph()

print(dfsRecursive(g,0))

