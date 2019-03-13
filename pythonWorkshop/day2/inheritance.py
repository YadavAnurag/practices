class Bird:

	def __init__(self):
		print('Bird is ready')

	def whoIsThis(self):
		print('Bird')

	def swim(self):
		print('Swim Faster')

class Parrot(Bird):
	def __init__(self):
		super().__init__()
		print('Parrot is ready')

	def whoIsThis(self):
		print('Parrot')

	def run(self):
		print('run faster')

parrot = Parrot()
parrot.whoIsThis()
parrot.swim()
parrot.run()

