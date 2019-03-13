class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high
	def __iter__(self):
		return self
	def next(self):
		if self.current<self.high:
			self.current = self.current+1
			return self.current
		else:
			raise StopIteration


c = Counter(5,10)
print(c)

print(c.next, c.next, c.next)



### generator

def Counter(low, high):
	current = low
	while current<=high:
		yield current
		current = current+1

