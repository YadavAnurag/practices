class student(object):
	def hello(self):
		print('Hello')
	def hi(self):
		print('Hi')

def callwhat(method):
	obj = student()
	getattr(obj, method)()

callwhat('hi')
callwhat('hello')