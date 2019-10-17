n = int(input())

s = ''.join([str(i+1) for i in range(n)])


res = ''
i = 0

if n%2==0:
	while i<len(s):
		res += (s[i+1]+s[i])
		i += 2
	print(*res)
else:
	print(-1)

