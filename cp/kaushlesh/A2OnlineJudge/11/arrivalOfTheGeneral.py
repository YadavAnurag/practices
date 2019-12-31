import sys
n = int(input())
elems = list(map(int, input().split()))
hid, lid = -1,-1
high,low = -sys.maxsize-1, sys.maxsize

for index,elem in enumerate(elems):
	if elem>high:
		hid = index
		high = elem

i = hid
count = 0
while (elems[0] != high) and i!=0:
	elems[i-1],elems[i] = elems[i],elems[i-1]
	count += 1
	i -= 1

for index,elem in enumerate(elems):
	if elem<=low:
		lid = index
		low = elem
i = lid

while (elems[-1] != low) and i!=(n-1):
	elems[i+1],elems[i] = elems[i],elems[i+1]
	count += 1
	i += 1

print(count)