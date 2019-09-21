for _ in range(int(input())):
	n,c,k = map(int, input().split())
	elem = list(map(int, input().split()))

	elemSum = 0
	i,j = 0,0
	while elemSum!=c:
		elemSum = sum(elem[i:j])
		j += 1
	print(i,j)