def solve(A,B):
	ans = 1

	def binExponentiation(num, p):
		res = num
		if p%2==1:
			res *= p
			p -= 1
		i = 2
		while i<=p:
			res**i


	for num in A:
		num = num%B
		ans = num**ans
	return ans%B

#print(solve([296, 383, 79, 1630, 1640, 1913, 520, 154, 932, 578, 707, 1449, 73, 1300, 475], 393))
print(solve([1,2,4,6], 10))