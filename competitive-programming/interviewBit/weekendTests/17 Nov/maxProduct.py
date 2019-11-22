def solve(A):
	A.sort()
	avg = sum(A)/2

	res = 0
	i = 0
	print(avg)
	flag = True
	while avg>res and i<len(A):
		if flag:
			flag = not flag
			res += A[i]
			print('included', A[i])
		else:
			res += A[-(i+1)]
			flag = not flag
			print('included', A[i])
		i += 1
	if res>avg:
		res -= A[i-1]
	print(res)
	return res*(sum(A)-res)
print(solve([1,1,2,2]))
print(solve([1,3,7,1]))