class LinkedList(object):
	class Node(object):
		def __init__(self, data, n=None):
			self.data = data
			self.next = n

	def __init__(sefl):
		self.head = None

