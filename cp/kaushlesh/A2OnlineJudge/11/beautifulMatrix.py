mat = []

rows,cols = 5,5
for _ in range(rows):
	row = list(map(int, input().split()))
	mat.append(row)	

mid = (2,2)
temp = ()
for id1, i in enumerate(mat):
	for id2, j in enumerate(i):
		if j==1:
			temp = (id1, id2)

a = abs(mid[0]-temp[0])
b = abs(mid[1]-temp[1])
print(a+b)