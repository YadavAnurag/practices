n = int(input())
mylist = list(map(int, input().split()))

count = 0

i=0
while i<n-2:
	print(i)
	if mylist[i+2] is 0:
		i += 2
		count += 1
	else:
		i += 1
		count += 1


print(count)
