class mylist(object):
	def __init__(self, a):
		self.alist = a
	def append(self,elem):
		self.alist.append(elem.upper())
	def pop(self, index):
		print('no pop')
	def __getattr__(self, method):
		return getattr(self.alist, method)

b = [1,2,3,12]
obj = mylist(b)

obj.sort(reverse=True)
print(b)


# multithreading is not the sol of concurrency in python bcz 
# 1. Python env is single threaded
# 2. While doing context switching one thread has to release the lock(GIL global interpreter lock) before other thread can acquire it-> this adds to overtime.
