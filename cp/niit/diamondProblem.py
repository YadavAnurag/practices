class A:
	def call(self):
		pass

class B1(A):
	def call(self):
		print('Its B1')
class B2(A):
	def call(self):
		print('Its B2')
class B3(A):
	def call(self):
		print('Its B3')

class C(B2, B1, B3):
	def whichCall(self):
		self.call()
	def restructure(self, parent1, parent2, parent3):
		self.__class__.__bases__ = (parent1, parent2, parent3)
	def printBaseClasses(self):
		print(self.__class__.__bases__)

c = C()
c.whichCall()
c.printBaseClasses()
c.restructure(B3, B2, B1)
c.printBaseClasses()

c.whichCall()