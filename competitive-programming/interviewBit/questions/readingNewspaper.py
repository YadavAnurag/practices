def solve(A,B):

	i,n = 0,len(B)
	while A>0:
		A -= B[i%n]
		i += 1

	if i%n==0:
		return 7
	return i%n
print(solve(433,[ 109, 58, 77, 10, 39, 125, 15 ]))
