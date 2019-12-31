# undirected graph
def bfs(g, s):
    queue = []
    visited = []

    queue.append(s)
    visited.append(s)

    while len(queue) is not 0:
        v = queue.pop(0)
        visited.append(v)
        for n in g[v]:
            if n not in visited:
                queue.append(n)
                visited.append(n)

g = {}
n,e = map(int, input().split())

for _ in range(e):
    v1,v2 = map(int, input().split())
    if v1 not in g.keys():
        g[v1] = [v2]
    else: g[v1].append(v2)
    
    if v2 not in g.keys():
        g[v2] = [v1]
    else:
        g[v2].append(v1)
