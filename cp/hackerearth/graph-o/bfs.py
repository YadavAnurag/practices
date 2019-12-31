def bfs(g,s):
	queue = []
	visited = []
	queue.append(s)
	visited.append(s)
	print('Root ->',s)
	while queue!=[]:
		v = queue.pop(0)
		for n in g[v]:
			if n not in visited:
				queue.append(n)
				visited.append(n)
				print('{} -> {}'.format(v,n))


g = {}
n,e = map(int, input().split())

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

bfs(g,0)