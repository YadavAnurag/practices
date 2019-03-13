import time

def decorate(fn):
	def wrapped(*args):
		a = time.time()
		print('before actual call {}'.format(str(a)))
		fn(*args)
		b = time.time()
		print('time taken for {} = {}'.format(fn.__name__, str(b)))
	return wrapped

@decorate
def anu():
	print('anu')
@decorate
def hello():
	print('Hi')

anu()
hello()