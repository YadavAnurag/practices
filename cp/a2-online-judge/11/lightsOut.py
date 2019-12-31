mat = [[1,1,1],[1,1,1], [1,1,1]]
op = []
rows, cols = 3, 3

for i in range(rows):
	op.append(list(map(int, input().split())))

op = [[1,0,0],[0,0,0],[0,0,0],[1,1,1]]
print(mat,'first', op, sep='\n')
for i in range(rows):
	for j in range(cols):
		temp = op[i][j]
		for k in range(temp):
			print('k', k)
			row, col = i, j
			while row!=-1:
				mat[row][col] = mat[row][col] ^ 1
				row -= 1
			while row!=2:
				mat[row][col] = mat[row][col] ^ 1
				row += 1
			while col!=-1:
				mat[row][col] = mat[row][col] ^ 1
				col -= 1
			while col!=2:
				mat[row][col] = mat[row][col] ^ 1
				col += 1
			# for l in range(3):
			# 	print('i,l',i,l)
			# 	mat[i][l] = mat[i][l] ^ 1
			# 	mat[l][i] = mat[l][i] ^ 1
print('ans')				
print(mat)