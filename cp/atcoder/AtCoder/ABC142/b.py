n, k = map(int, input().split())
elems = map(int, input().split())

count = 0
for elem in elems:
	if(elem>=k):
		count += 1
print(count)