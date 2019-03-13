Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/caller.py ==
>>> import caller
>>> 
=============================== RESTART: Shell ===============================
>>> a =  lambda x,y :  x+y
>>> a
<function <lambda> at 0x0420A3D8>
>>> a(3,4)
7
>>> n = [1,2,3,4,5,6]
>>> y = [7,8,9,2,3,4]
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> n
[1, 2, 3, 4, 5, 6]
>>> y
[7, 8, 9, 2, 3, 4]
>>> map(lambda x,y: x+y , n,y)
<map object at 0x04207FF0>
>>> 
KeyboardInterrupt
>>> map(lambda x,y: x+y , n,y)()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    map(lambda x,y: x+y , n,y)()
TypeError: 'map' object is not callable
>>> for elem in map:
	print (elem)

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for elem in map:
TypeError: 'type' object is not iterable
>>> f = map(lambda x,y: x+y , n,y)
>>> dir(f)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> f = map(lambda x: x*x , n)
>>> f
<map object at 0x04207FF0>
>>> dir(f)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> f.__sizeof__()
16
>>> x
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> n
[1, 2, 3, 4, 5, 6]
>>> f.__repr__()
'<map object at 0x04207FF0>'
>>> f.next()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    f.next()
AttributeError: 'map' object has no attribute 'next'
>>> f.__next__()
1
>>> f.__next()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f.__next()
AttributeError: 'map' object has no attribute '__next'
>>> f.__next__()
4
>>> map
<class 'map'>
>>> a =  map(lambda x :  x*x*x , [3,4,5,6,7,8,32,21])
>>> a
<map object at 0x01562CD0>
>>> a.__next__()
27
>>> a.__next__()
64
>>> a.__next__()
125
>>> a.__next__()
216
>>> a.__next__()
343
>>> a.__next__()
512
>>> a.__next__()
32768
>>>  
