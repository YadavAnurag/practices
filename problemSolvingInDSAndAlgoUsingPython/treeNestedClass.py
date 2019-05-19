class Tree(object):
	class Node(object):
		def __init__(self, v, l=None, r=None):
			self.value = v
			self.lchild = l
			self.rchild = r 

	def __init__(self):
		self.root = None

