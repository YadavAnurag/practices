import re

n = int(input())
s = input()

count=0
if not bool(re.match('.*[0-9].*', s)):
	print('0','not match')
	count+=1
if not bool(re.match('.*[a-z].*', s)):
	print('a','not match')
	count+=1
if not bool(re.match('.*[A-Z].*', s)):
	print('A','not match')
	count+=1
if not bool(re.match('.*[!@#%\^\$\*\(\)\-+].*', s)):
	print('&','not match')
	count+=1

if len(s)>=6 or (len(s)+count)>=6:
	print(count)
else:
	print(6-len(s))


