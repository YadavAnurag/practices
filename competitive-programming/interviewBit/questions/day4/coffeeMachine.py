from abc import ABCMeta, abstractmethod

class CoffeeInterface():
	__metaclass__ = ABCMeta

	def __init__(self):
		self.ingredients = ['Milk', 'Water', 'Coca Powder', 'Sugar', 'Coffee Powder']

	def addIngredients(self, ingredient):
		raise NotIm
		plementedError

	def displayIngredients(self):
		print(*self.ingredients, sep='\n')

class Coffee(CoffeeInterface):
	def __init__(self):
		super().__init__()
	def addIngredients(self, ingredient):
		print('someehing')
		self.ingredients.append(ingredient)

c = Coffee()
c.addIngredients('first')
c.displayIngredients()
