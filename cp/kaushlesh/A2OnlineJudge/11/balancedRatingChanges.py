import math
n = int(input())

elems = []
for _ in range(n):
	elems.append(int(input()))

res = []
flag = 0
for index, elem in enumerate(elems):
	if elem<0 and elem%2==1:
		if flag == 1:
			res.append(math.ceil(elem/2))
			flag = 0
		elif flag == 0:
			res.append(math.floor(elem/2))
			flag = 1
	else:
		res.append(elem//2)

print(res,sum(res))
i = 0
while sum(res)!=0 and i<len(res):
	if elems[i]<0 and elems[i]%2==1:
		res[i] = math.floor(elems[i]/2)
	i += 1
print(res,sum(res))
print(*res, sep="\n")