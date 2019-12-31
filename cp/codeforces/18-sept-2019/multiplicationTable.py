n = int(input())
mat = []

for _ in range(n):
	mat.append(list(map(int, input().split())))
m = n//2
mid = ((mat[m][m-1]*mat[m+1][m])/(mat[m-1][m+1]))

mid = mid**0.5
mylist = []
for i in range(n):
	if(i==m):
		mylist.append(int(mid))
	else:
		mylist.append(int(mat[i][m]/int(mid)))
print(*mylist)

