a,b,n = map(int, input().split())

p1,p2 = 2,2
total = set([a,b])
prev = 2

while n-2:
	temp = 0
	if a*p1<b*p2:
		temp = a*p1
		p1 += 1
	else:
		temp = b*p2
		p2 += 1

	total.add(temp)
	if prev == len(total):
		pass
	else:
		print(temp, total)
		prev += 1
		n -= 1