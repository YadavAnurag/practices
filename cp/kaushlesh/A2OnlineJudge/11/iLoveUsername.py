import sys
n = int(input())
elems = list(map(int, input().split()))
low,high = elems[0], elems[0]

count = 0
for elem in elems:
	if elem>high:
		count += 1
		high = elem
	if elem<low:
		count += 1
		low = elem
print(count)
