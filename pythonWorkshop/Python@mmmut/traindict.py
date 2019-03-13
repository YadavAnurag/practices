Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> d = {"name":"pawan","company":"practo","college":"mmm"}
>>> d
{'name': 'pawan', 'company': 'practo', 'college': 'mmm'}
>>> d['name']
'pawan'
>>> d['college']
'mmm'
>>> d['test'] = 56
>>> d
{'name': 'pawan', 'company': 'practo', 'college': 'mmm', 'test': 56}
>>> d['abc']= 'xyz'
>>> d
{'name': 'pawan', 'company': 'practo', 'college': 'mmm', 'test': 56, 'abc': 'xyz'}
>>> d.keys()
dict_keys(['name', 'company', 'college', 'test', 'abc'])
>>> d.values()
dict_values(['pawan', 'practo', 'mmm', 56, 'xyz'])
>>> d.items()
dict_items([('name', 'pawan'), ('company', 'practo'), ('college', 'mmm'), ('test', 56), ('abc', 'xyz')])
>>> for elem in d.items():
	print (elem)

	
('name', 'pawan')
('company', 'practo')
('college', 'mmm')
('test', 56)
('abc', 'xyz')
>>> 
KeyboardInterrupt
>>> for elem in d.items():
	str1 = "the value for key " +str(elem[0]) + " = " + str(elem[1])

	
>>> for elem in d.items():
	str1 = "the value for key " +str(elem[0]) + " = " + str(elem[1])
	print (str1)

	
the value for key name = pawan
the value for key company = practo
the value for key college = mmm
the value for key test = 56
the value for key abc = xyz
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
