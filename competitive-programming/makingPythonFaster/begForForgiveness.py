class Foo(object):
	hello = 'world'
foo = Foo()



'''
	taking persmission if it is then do any task
	149 ns
'''
if hasattr(foo, 'hello'):
	print(foo.hello)



'''
	beg for forgiveness
	43.1 ns
'''
try:
	print(foo.hello)
except AttributeError:
	pass
