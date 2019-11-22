def solve(A):
	ans = 0
	for i in range(len(A)):
		ans += (ord(A[-(i+1)])-64)*(26**i)
	return ans
print(solve('ZPKR'))
