n = int(input())
mylist = list(map(int, input().split()))

evenCount = 0
oddCount = 0

for i in range(len(mylist)):
	if mylist[i]%2 == 0:
		evenCount += 1
	else:
		oddCount += 1

print(min(evenCount, oddCount))
