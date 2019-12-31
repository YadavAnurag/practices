def solve(A,B):
	a,b = A,B
	while B:
		A,B = B, A%B
	

	return A


print(solve(2549,7))