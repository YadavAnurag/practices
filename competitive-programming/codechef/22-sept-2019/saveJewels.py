for _ in range(int(input())):
	n,m = map(int, input().split())
	prices = list(map(int, input().split()))

	elem = prices[:]
	days = []
	for i in range(m):
		l,r = map(int, input().split())
		days.append((l,r))
	flag = -1
	mainFlag = -1
	maxCurrent  =0
	for i in range(len(days)):
		l,r = days[i]
		current = 0
		for j in range(len(elem[l-1:r])):
			if elem[j]>current:
				current = elem[j]
				flag = j
		elem[flag+l-1] = 0 

		itsum = sum(elem[l-1:r])
		if itsum>maxCurrent:
			maxCurrent = itsum
			mainFlag = i
	print('mainFlag', mainFlag)