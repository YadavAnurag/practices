1. 
def solve(a, b):
	i,j = 0,0
	m,n = len(a),len(b)
	while i<m and j<n:
		if a[i]==b[j]:
			i += 1
		j += 1
	return i==m
print(solve('ag', 'anurag'))



def solve1(N, operations):
	r = [0]*N 
	c = [0]*N

	for c, i, x  in operations:
		if c=='c':
			c[i] += x
		if c=='r':
			r[i] += x 

	return(max(c)+max(r))


print(solve1(3, [('r',0,3),('c',1,5),('r',0,5),('r',0,1)]))