class myStack:
	def __init__(self):
		self.stackList = []

	def isEmpty(self):
		return len(self.stackList)==0

	def top(self):
		if self.isEmpty():
			return None
		return self.stackList[-1]

	def size(self):
		return len(self.stackList)

	def push(self, value):
		self.stackList.append(value)

	def pop(self):
		if self.isEmpty():
			return None
		return self.stackList.pop()



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



def reverse(queue,k):
	mystack = myStack()

	for i in range(k):
		mystack.push(queue.dequeue())

	while not mystack.isEmpty():
		queue.enqueue(mystack.pop())

		
	for i in range(len(queue.queueList)-k):
		queue.enqueue(queue.dequeue())



queue = myQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)

print(queue.front())
print(queue.back())

reverse(queue,5)
while not queue.isEmpty():
	print(queue.dequeue())