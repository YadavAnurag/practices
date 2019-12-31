from abstractClass import Shape
import math

class Circle(object):
	def __init__(self, r):
		self.radius = r 

	def setRadius(self, r):
		self.radius = r 

	def area(self):
		return math.pi*self.radius**2

	def perimeter(self):
		return 2*math.pi*self.radius

	@classmethod
	def radius(self):
		print(self.radius)

print(Circle.radius())


c = Circle(2)

print(c.area())
