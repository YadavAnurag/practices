Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class student:
	pass

>>> student.__class__
<class 'type'>
>>> class student(object):
	pass

>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/diamond.py =
100
>>> class student:
	pass

>>> student
<class '__main__.student'>
>>> id(student)
68650424
>>> 
>>> 

>>> hello =  student
>>> helolo
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    helolo
NameError: name 'helolo' is not defined
>>> hello
<class '__main__.student'>
>>> student
<class '__main__.student'>
>>> id(hello)
68650424
>>> id(student)
68650424
>>> class student:
	def hello(self):
		print (self)
		print ("ddsddsd")

		
>>> ritik = student()
>>> ritik
<__main__.student object at 0x04167C50>
>>> shashwat =  student()
>>> shashwat
<__main__.student object at 0x04167B50>
>>> ritik.hello()
<__main__.student object at 0x04167C50>
ddsddsd
>>> shashwat.hello()
<__main__.student object at 0x04167B50>
ddsddsd
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py ==
heello
9
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py ==
heello
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py", line 10, in <module>
    obj.hi(1,4,5)
TypeError: hi() takes 3 positional arguments but 4 were given
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py ==
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py", line 11, in <module>
    obj =  student()
TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py ==
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py", line 12, in <module>
    obj.hi()
  File "C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py", line 8, in hi
    d =  c + d
NameError: name 'c' is not defined
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python37-32/class1.py ==
70
>>> 
