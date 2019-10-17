for _ in range(int(input())):
	n = int(input())
	arr = [[] for i in range(n)]

	count = 1
	for sm in range(2*n-2):
		for row in range(n):
			col =  sm-row
			if((0<=col) and (n>col)):
				arr[row][col] += count
				count += 1
	print(arr)