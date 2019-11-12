def solve(A):

	i = 0
	gmax = 0
	prevFirst, prevSecond = -1, -1
	currFirst, currSecond = -1, -1
	while i<len(A):
		flag,first = 1,i		
		lmax = 0

		while i<len(A) and A[i]>=0:
			lmax += A[i]
			i += 1	
			flag = 0

		if flag: i += 1

		if currFirst==-1:
			prevFirst, prevSecond = first, i
			currFirst, currSecond = first, i 


		if gmax < lmax:
			currFirst, currSecond = first,i
			gmax = max(gmax, lmax)
		elif gmax==lmax:
			if (currSecond - currFirst) < (prevSecond - prevFirst):
				 currFirst, currSecond = prevFirst, prevSecond
				 gmax = max(gmax, lmax)
			elif (currSecond - currFirst) == (prevSecond - prevFirst):
				currFirst, currSecond = prevFirst, prevSecond

	if A[currFirst:currSecond][0] < 0:
		return []
	else:
		return A[currFirst:currSecond]

print(solve([0,0,-1,0]))
print(solve([-1,-1,-1,-1]))
print(solve([1, 2, 5, -7, 2, 3,3]))
print(solve([10, -1, 2, 3, -4, 100]))