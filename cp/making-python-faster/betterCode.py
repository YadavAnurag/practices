'''
1.
looping backward
'''
a = [1,2,3]
for i in reversed(a):
	print(i)


'''
2.
looping over two collections
use zip
'''
a = [1,2,3]
b = ['a','b','c']

for i,j in zip(a,b):
	print(i,j)


'''
3.
custom sort 
'''
colors = ['red', 'green', 'black']
sorted(colors, key=len)
print(colors)

       
itr = iter(colors)
print(next(itr))
print(next(itr))
print(next(itr))

for i in iter(colors):
	print(i)


'''
4.
for else

if foor loop exit normalyy
then else block will execute
'''
def forElse():
	for i in range(10):
		if i==60:
			break
	else:
		return -1
	return 1

'''
5.
looping dict
'''
colors = {'anu':'red', 'mahesh':'green', 'kaushlesh':'black','ravish':'red', 'shankar':'green', 'shivam':'black'}
d = {c: colors[c] for c in colors if not c.startswith('r')}
print(d)
