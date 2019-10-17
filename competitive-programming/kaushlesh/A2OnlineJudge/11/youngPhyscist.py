n = int(input())

elems = []
for i in range(n):
	elems.append(list(map(int, input().split())))

res = []
for i in zip(*elems):
	res.append(sum(i))

print('YES') if res[0]==0 and res[1]==0 and res[2]==0 else print("NO")

	