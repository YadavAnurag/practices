def solve(A):
	ans = ''
	while A!=0:
		A, mod = divmod(A, 26)
		if mod==0:
			A,mod = A-1, mod+26

		a = chr(mod+64)
		ans += a
	return ans[::-1]
print(solve(943566))