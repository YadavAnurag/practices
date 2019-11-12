def solve(A):
	if len(A)<2:
		return 0
	B = list(A)
	B.sort()

	i,gmax = 1,-10**6
	while i<len(B):
		gmax = max(abs(B[i]-B[i-1]), gmax)
		i += 1
	if gmax == -10**6:
		return 0
	else:
		return gmax

print(solve([1, 10, 5]))
print(solve([-1, -2, -3, -5]))
print(solve([0,0,0]))
print(solve([0]))
print(solve([100,100,100]))