n = int(input())
primes = [False, False]+[True]*(n-1)

p = 2
while p**2<=n:
	if primes[p]:
		for i in range(2*p, n+1, p):
			primes[i] = False
		p += 1

for i in range(n+1):
	if primes[i]:
		print(i)