Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> a = "7411089959 is my mobile number"
>>> b  = re.search("\d+",a)
>>> 
>>> b
<re.Match object; span=(0, 10), match='7411089959'>
>>> b.group()
'7411089959'
>>> a = "my mobile number is 7411089959"
>>> b  = re.search("\d+",a)
>>> b.group()
'7411089959'
>>> '7411089959'
'7411089959'
>>> a
'my mobile number is 7411089959'
>>> b  = re.search("\d*",a)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b
<re.Match object; span=(0, 0), match=''>
>>> b.group()
''
>>> a = "7411089959 is my mobile number"
>>> b  = re.search("\d*",a)
>>> b
<re.Match object; span=(0, 10), match='7411089959'>
>>> b.group()
'7411089959'
>>> a
'7411089959 is my mobile number'
>>> b  = re.search("\d{3,6}",a)
>>> b
<re.Match object; span=(0, 6), match='741108'>
>>> b.group()
SyntaxError: invalid syntax
>>> 
>>> b
<re.Match object; span=(0, 6), match='741108'>
>>> b.group()
'741108'
>>> a
'7411089959 is my mobile number'
>>> b  = re.search("\d{6}",a)
>>> b.group()
'741108'
>>> a = "32 is my age and 7411089959 is my number"
>>> b = re.search("\d*",a)
>>> b
<re.Match object; span=(0, 2), match='32'>
>>> b.group()
'32'
>>> b = re.search("\d{3,10}",a)
>>> b.group()
'7411089959'
>>> 

>>> a = "7my mame"
>>> b = re.search("\d+",a)
>>> b.group()
'7'
>>> b = re.search("\d*",a)
>>> b = re.search("\d+",a)
>>> b.group()
'7'
>>> a = "7my mame 8878"
>>> b = re.search("\d+",a)
>>> b.group()
'7'
>>> a
'7my mame 8878'
>>> b = re.search("\d+",a)
>>> b.group()
'7'
>>> b = re.search("\d*",a)
>>> b.group()
'7'
>>> b = re.search("\d{2,89}",a)
>>> a
'7my mame 8878'
>>> b.group()
'8878'
>>> 
