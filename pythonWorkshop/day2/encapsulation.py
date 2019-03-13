class Computer:
	#__maxprice = 56
	def __init__(self):
		self.__maxprice = 9000

	def sell(self):
		print('selling price is {}'.format(self.__maxprice))

	def setMaxPrice(self, price):
		self.__maxprice = price 



c = Computer()
c.sell()

c.setMaxPrice(10000)
c.__maxprice = 2222222222
c.sell()

print(c.__maxprice)
c.sell()