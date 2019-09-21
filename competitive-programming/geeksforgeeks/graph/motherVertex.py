from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def dfsUtil(self, v, visited):
		visited[v] = True
		print('Visiting ',v)

		for i in graph[v]:
			if visited[i] == False:
				self.dfsUtil(i, visited)

	def dfs(self, s):
		visited = [False]*len(self.graph)
		self.dfsUtil(s, visited)



