def solve(A,B):

	while B:
		A,B = B, A%B
	return A

print(solve(3,6))