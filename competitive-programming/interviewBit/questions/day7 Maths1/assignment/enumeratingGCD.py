def solve(A,B):
	if A==B:
		return A

	p = int(A)
	q = int(B)

	if p<q:
		p,q = q,p
		
	def gcd(p,q):
		while q:
			p,q = q,p%q 
		return p

	g = gcd(p,p+1)
	for i in range(p+1, q+1):
		g = gcd(g, i)
		if g==1:
			return 1
	return g

		
print(solve(0,3))
		


	