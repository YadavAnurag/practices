for _ in range(int(input())):
	s = input()
	expected = 'hackerrank'
	p=0
	for i in range(len(s)):
		if s[i]==expected[p]:
			p+=1
			if len(expected)==p:
				break
	if len(expected)==p:
		print('YES')
	else:
		print('NO')