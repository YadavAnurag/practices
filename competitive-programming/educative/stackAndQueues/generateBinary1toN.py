class myQueue:
	def __init__(self):
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



def findBianry(n):
	queue = myQueue()
	mylist = []
	queue.enqueue(1)

	for i in range(n):
		mylist.append(str(queue.dequeue()))
		s1 = mylist[i] + "0"
		s2 = mylist[i] + "1"

		queue.enqueue(s1)
		queue.enqueue(s2)
	return mylist

print(findBianry(2))