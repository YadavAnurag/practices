def solve(A):

	i = 0
	while A:
		A = A//2
		i += 1
	return 2**(i-1)
print(solve(6))