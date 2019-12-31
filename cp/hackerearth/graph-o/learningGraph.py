from collections import OrderedDict as od

g = od()

n,e,k = map(int, input().split())
mylist = list(map(int, input().split()))

for i in range(len(mylist)):
	g[mylist[i]] = [] 

print(g)
for _ in range(e):
	a,b = map(int, input().split())
	g[a].append(b)
	g[b].append(a)
print(g)
