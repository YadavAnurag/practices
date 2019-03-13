Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 30
>>> type(a)
<class 'int'>
>>> a =  30.5
>>> type(a)
<class 'float'>
>>> a = "mmmec"
>>> type(a)
<class 'str'>
>>> a  = 27832893293
>>> type(a)
<class 'int'>
>>> a =  34343353534534535
>>> type(a)
<class 'int'>
>>> a = 7783289023023023203
>>> type(a)
<class 'int'>
>>> 
>>> 
>>> 
>>> 
>>> 

>>> a
7783289023023023203
>>> 
>>> 
>>> 
>>> b = 'pawan'
>>> 3 + 4
7
>>> "pawan" + "pundir"
'pawanpundir'
>>> a
7783289023023023203
>>> b
'pawan'
>>> a +  b
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a +  b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> #####
>>> a =  34
>>> a.__class__
<class 'int'>
>>> d = 56.7
>>> d.__class__
<class 'float'>
>>> ####
>>> a = [12,45,67]
>>> type(a)
<class 'list'>
>>> a = (1,4,5)
>>> type(a)
<class 'tuple'>
>>> a = {"name":"pawan","age":32,"company":"practo"}
>>> type(a)
<class 'dict'>
>>> a.__class__
<class 'dict'>
>>> 
>>> 
>>> 

>>> 
>>> a = [1,45,65,65,76]
>>> a[0]
1
>>> a[1]
45
>>> a[2]
65
>>> n =  len(a)
>>> n
5
>>> a[n-1]
76
>>> a
[1, 45, 65, 65, 76]
>>> a[-1]
76
>>> a[-2]
65
>>> 
>>> a = [2,3,4,67,32]
>>> b =  a
>>> 
>>> 
>>> b.append(34)
>>> b
[2, 3, 4, 67, 32, 34]
>>> a
[2, 3, 4, 67, 32, 34]
>>> id(a)
55479472
>>> 
>>> 
>>> id(b)
55479472

>>> 
>>> a
[2, 3, 4, 67, 32, 34]
>>> b
[2, 3, 4, 67, 32, 34]
>>> import copy
>>> b = copy.copy(a)
>>> 
>>> 
>>> b
[2, 3, 4, 67, 32, 34]
>>> a
[2, 3, 4, 67, 32, 34]
>>> id(a)
55479472
>>> id(b)
51042144
>>> b
[2, 3, 4, 67, 32, 34]
>>> a
[2, 3, 4, 67, 32, 34]
>>> b.append(90)
>>> b
[2, 3, 4, 67, 32, 34, 90]
>>> a
[2, 3, 4, 67, 32, 34]
>>> 
>>> 
>>> 
>>> ###
>>> 
>>> a
[2, 3, 4, 67, 32, 34]

>>> 
>>> a[0]
2
>>> a.append(97)
>>> a
[2, 3, 4, 67, 32, 34, 97]
>>> a.insert(1,89)
>>> a
[2, 89, 3, 4, 67, 32, 34, 97]
>>> a.insert(0,56)
>>> a
[56, 2, 89, 3, 4, 67, 32, 34, 97]
>>> for elem in a:
	print (elem)

	
56
2
89
3
4
67
32
34
97
>>> a
[56, 2, 89, 3, 4, 67, 32, 34, 97]
>>> 
>>> 
>>> a.pop(1)
2
>>> a
[56, 89, 3, 4, 67, 32, 34, 97]
>>> a.pop(0)
56
a
>>> 
>>> a
[89, 3, 4, 67, 32, 34, 97]
>>> a.pop()
97
>>> a
[89, 3, 4, 67, 32, 34]
>>> 
>>> 
>>> 
>>> a.sort()
>>> a
[3, 4, 32, 34, 67, 89]
>>> a.sort(reverse=True)
>>> a
[89, 67, 34, 32, 4, 3]
>>> #######
>>> 
>>> 
>>> 
>>> ###stack
>>> a
[89, 67, 34, 32, 4, 3]
>>> a.append(67)
>>> a
[89, 67, 34, 32, 4, 3, 67]
>>> a.pop()
67
>>> #####
>>> a
[89, 67, 34, 32, 4, 3]
>>> ####
>>> queue
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    queue
NameError: name 'queue' is not defined

>>> #queue
>>> a
[89, 67, 34, 32, 4, 3]
>>> a.append(90)
>>> a
[89, 67, 34, 32, 4, 3, 90]
>>> a.pop(0)
89
>>> ####
>>> a = {"name":"pawan","age":32,"company":"practo"}
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    a[0]
KeyError: 0
>>> a["name"]
'pawan'
>>> a["age"]
32
>>> a["college"] = "mmm"
>>> a
{'name': 'pawan', 'age': 32, 'company': 'practo', 'college': 'mmm'}
>>> a.keys()
dict_keys(['name', 'age', 'company', 'college'])
>>> 
>>> a.values()
dict_values(['pawan', 32, 'practo', 'mmm'])
>>> 
>>> a.items()
dict_items([('name', 'pawan'), ('age', 32), ('company', 'practo'), ('college', 'mmm')])
>>> for elem in a.items():
	print (elem)

	
('name', 'pawan')
('age', 32)
('company', 'practo')

('college', 'mmm')
>>> for elem in a.items():
	print ("value for key " + str(elem[0]) + "  =
	       
SyntaxError: EOL while scanning string literal
>>>  
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> for elem in a.items():
	       
KeyboardInterrupt
>>> for elem in a.items():
	       print ("val for key" + str(elem[0]) + "= " + str(elem[1]))

	       
val for keyname= pawan
val for keyage= 32
val for keycompany= practo
val for keycollege= mmm
>>> 
