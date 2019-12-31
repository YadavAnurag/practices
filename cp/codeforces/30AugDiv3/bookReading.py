for _ in range(int(input())):
	n,m = map(int, input().split())

	total = 0
	for i in range(1, n+1):
		if i%m == 0:
			total += int(str(i)[-1])
	print(total)