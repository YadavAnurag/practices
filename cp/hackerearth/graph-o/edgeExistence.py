n,e = map(int, input().split())

g = {}

for _ in range(e):
	n1,n2 = map(int, input().split())
	if n1 in g.keys():
		g[n1].append(n2)
	else:
		g[n1] = [n2]
	if n2 in g.keys():
		g[n2].append(n1)
	else:
		g[n2] = [n1]

q = int(input())

for _ in range(q):
	a,b = map(int, input().split())
	if a in g.keys() and b in g.keys():
		if b in g[a] and a in g[b]:
			print('YES')
		else:
			print('NO')
	else:
		print('NO')


