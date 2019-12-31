n = int(input())
elems = list(map(int, input().split()))

ranges = [i for i in range(1, len(elems)+1)]
myElems = zip(elems, ranges)
newElems = sorted(myElems, key=lambda x: x[0])


res = []
for _,i in newElems:
	res.append(i)
print(*res)









# a = [(1, 2), (25, 1), (9, 4)]
# a.sort(key=lambda x: x[0])
# print(a)