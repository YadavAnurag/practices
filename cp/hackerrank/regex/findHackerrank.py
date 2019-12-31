for _ in range(int(input())):
	s = input()
	if s.startswith('hackerrank') and s.endswith('hackerrank'):
		print(0)
	elif s.startswith('hackerrank'):
		print(1)
	elif s.endswith('hackerrank'):
		print(2)
	else:
		print(-1)
