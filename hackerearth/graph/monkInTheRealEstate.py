for _ in range(int(input())):
	myset = set()
	for _ in range(int(input())):
		a,b = map(int, input().split())
		myset.add(a)
		myset.add(b)
	print(len(myset))
