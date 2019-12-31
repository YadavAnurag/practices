class Stack:
	def __init__(self):	
		self.items = []
	def isEmpty(self):
		return len(self.items) is 0
	def push(self, item):
		self.items.append(item)
	def pop(self):
		if self.items is not []:
			return self.items.pop()
	def peek(self):
		if self.isEmpty() is False:
			return self.items[-1]

a = Stack()
a.push(1)
print(a.pop())
print(a.peek())
print(a.isEmpty())

