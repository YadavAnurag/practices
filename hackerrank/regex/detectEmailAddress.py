import re
s = ''
emaliList = []
for _ in range(int(input())):
	s += input()
emaliList += re.findall(r'[a-zA-Z]+\.[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+',s)
print(*emaliList,sep=";")
print(len(emaliList))


