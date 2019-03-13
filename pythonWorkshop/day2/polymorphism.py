class Parrot:
	def fly(self):
		print('Parrot can fly')

class Penguin:
	def fly(self):
		print('Penguin can not fly')


# common method
def flyingTest(bird):
	bird.fly()

blu = Parrot()
peggy = Penguin()

flyingTest(blu)
flyingTest(peggy)