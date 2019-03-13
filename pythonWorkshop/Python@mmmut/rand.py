Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class student(object):
	def hello(self):
		print ("hello")
	def hi(self):
		print ("hi")

		
>>> obj = student()
>>> obj.hello()
hello
>>> obj.hi()
hi
>>> def callwhat(method):
	obj = student()
	getattr(obj,method)()

	
>>> callwhat("hello")
hello
>>> 
>>> 
>>> 
>>> 
>>> callwhat
<function callwhat at 0x03BCA3D8>
>>> callwhat("hi")
hi
>>> callwhat("pawan")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    callwhat("pawan")
  File "<pyshell#15>", line 3, in callwhat
    getattr(obj,method)()
AttributeError: 'student' object has no attribute 'pawan'
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
[1, 2, 3, 'pawan']
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
[1, 2, 3, 'PAWAN']
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
[1, 2, 3, 'PAWAN']
u cannot pop
[1, 2, 3, 'PAWAN']
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
[1, 2, 3, 'PAWAN']
u cannot pop
[1, 2, 3, 'PAWAN']
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py", line 17, in <module>
    obj.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
u cannot pop
[1, 2, 3, 65, 43, 12]
[1, 2, 3, 12, 43, 65]
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
u cannot pop
[1, 2, 3, 65, 43, 12]
sort
[1, 2, 3, 12, 43, 65]
>>> reverse

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
u cannot pop
[1, 2, 3, 65, 43, 12]
sort
[1, 2, 3, 12, 43, 65]
reverse
[65, 43, 12, 3, 2, 1]
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
u cannot pop
[1, 2, 3, 65, 43, 12]
sort
[1, 2, 3, 12, 43, 65]
reverse
[65, 43, 12, 3, 2, 1]
insert
[45, 65, 43, 12, 3, 2, 1]
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
[1, 2, 3, 65, 43, 12, 'PAWAN']
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
u cannot pop
[1, 2, 3, 65, 43, 12]
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/delegate.py =
u cannot pop
[1, 2, 3, 65, 43, 12, 56]
>>> import random
>>> random.random()
0.29891948565423787
>>> random.random()
0.16307640395260714
>>> random.random()
0.12371234992233426
>>> random.random()
0.42638651200286104
>>> random.randint(10000,99999)
84365
>>> random.randint(10000,99999)
50249
>>> random.randint(10000,99999)
62697
>>> random.randint(10000,99999)
45086
>>> my_list=[]
>>> my_list.append([])
>>> my_list
[[]]
>>> my_list.append([])
>>> my_list
[[], []]
>>> import time
>>> a = time.time()
>>> a
1551517868.828222
>>> b = time.time()
>>> b
1551517876.9853487
>>> b - a
8.157126665115356
>>> 
