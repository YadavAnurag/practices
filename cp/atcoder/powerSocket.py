for _ in range(int(input())):
	n,m = map(int, input())

	count = 0
	while n<m:
		n += n
		count += 1

	print(count+1)