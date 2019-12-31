n, k, q = map(int, input().split())

arr = [k]*n

for _ in range(q):
	p = int(input())
	arr[p-1] += 1

for index, elem in enumerate(arr):
	if (arr[index]-q)<=0:
		print('No')
	else:
		print('Yes')