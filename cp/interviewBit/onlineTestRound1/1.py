def solve(n):
	if n<=128:
		return 1
	else:
		i = 2
		while True:
			if ((n+5*i)/i)<=128:
				return i
			i+=1
		