class Bulb(object):
	class BulbSize(object):
		SMALL = u'SMALL'
		MEDIUM = u'MEDIUM'
		LARGE = u'LARGE'
	def __init__(self):
		self.inOn = False
		self.size = Bulb.BulbSize.MEDIUM
	def getBulbSize(self):
		return self.size
	def setBulbSize(self, value):
		self.size = value
	
class BulbDemo(object):
	@classmethod
	def main(cls, args):
		b = Bulb()
		print(b.getBulbSize())

if __name__ == '__main__':
	import sys
	BulbDemo.main(sys.argv)		
