for i in range(int(input())):
	n,a,b = map(int, input().split())
	l = list(map(int, input().split()))
	c,bob,alice = 0,0,0
	for i in l:
		if(i%a==0 and i%b==0):
			c += 1
		else:
			if(i%a==0):
				bob += 1
			if(i%b==0):
				alice += 1
	if(c>0):
		bob += 1
	if(bob<=alice):
		print('ALICE')
	else:
		print('BOB')

