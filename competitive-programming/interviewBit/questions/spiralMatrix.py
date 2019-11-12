def solve(n):
	res = [[0 for _ in range(n)] for _ in range(n)]
	count = 1

	temp = n
	t = 0
	while(count < temp**2):
		for i in range(t, n-1+t):
			res[t][i] = count
			count += 1

		for i in range(t, n-1+t):
			res[i][n+t-1] = count
			count += 1
			
		for i in range(n-1+t, t, -1):
			res[n-1+t][i] = count
			count += 1

		for i in range(n-1+t, t, -1):
			res[i][t] = count
			count += 1

		n -= 2
		t += 1
	if temp%2 != 0:
		res[temp//2][temp//2] = count
	return res


print(solve(3))