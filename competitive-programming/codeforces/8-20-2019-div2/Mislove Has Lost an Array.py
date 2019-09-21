n,l,r = map(int, input().split())

minList, maxList = [1],[1]

elem = 1
for i in range(r-1):
	elem  = elem*2
	maxList.append(elem)
maxList += [elem]*(n-r)

elem = 1
for i in range(l-1):
	elem  = elem*2
	minList.append(elem)
minList = [1]*(n-l)+minList



print(sum(minList),sum(maxList))