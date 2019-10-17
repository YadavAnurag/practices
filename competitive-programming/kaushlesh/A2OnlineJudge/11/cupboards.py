n = int(input())

left, right = [],[]
for _ in range(n):
	a,b = map(int,input().split())
	left.append(a)
	right.append(b)

def cupboards(lef, right):
	lz,lo = 0,0
	rz, ro = 0,0

	for a,b in zip(left, right):
		if a:
			lo += 1
		else:
			lz += 1

		if b:
			ro += 1
		else:
			rz += 1

	if abs(lo-lz)==n and abs(ro-rz)==n:
		return 0
	
	count = 0
	if lz>lo:
		count += lo
	else:
		count += lz 
	
	if rz>ro:
		count += ro 
	else:
		count += rz 


	return count
print(cupboards(left, right))