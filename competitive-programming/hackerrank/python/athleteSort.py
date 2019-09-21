n,m = map(int, input().split())
mylist = []

for i in range(n):
	mylist.append(list(map(int, input().split())))


k = int(input())
arr = sorted(mylist, key=lambda x: x[k])

for i in range(n):
	print(*arr[i])

