class BinarySearch(object):
	def __init__(self):
		self.l=0
		self.r=0
		self.mid=0
		

	def findNum(self, mylist, value):
		self.r = len(mylist)-1
		self.mid = (self.l+(self.r-self.l))//2
		print(self.mid)
		while self.l<=self.mid:
			if mylist[self.mid] == value:
				return self.mid
			else:
				if mylist[self.mid] < value:
					self.l = self.mid+1
				else:
					self.r = self.mid-1
			print(self.l, self.r, self.mid)
		return False

bs1 = BinarySearch()
bs2 = BinarySearch()

print(bs1.findNum([1,2,3,3,4,5,6], 5), bs2.findNum([1,2,3,3,4,5,6], 9))
