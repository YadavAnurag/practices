(n, m) = map(int, input().split(' '))
myList = list(map(int, input().split(' ')))
count = 0
found = False
for i in range(n-1, 0, -1):
	if(found):
		break
	if(myList[i]==m):
		count = i
		found = True
		break
if(found):
	print(count+1)
else:
	print(-1)
