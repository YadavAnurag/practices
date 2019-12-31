def getFinal(A,B):
	if A==0 or B==0:
		return A+B
	if A<B:
		A,B = B,A
	while B:
		A,B = B,A%B
	return 2*A

print(getFinal(3,8))