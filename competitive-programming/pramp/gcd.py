def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

def gcd1(a,b):
	while b:
		a,b = b, a%b
	return a

print(gcd1(60, 48))