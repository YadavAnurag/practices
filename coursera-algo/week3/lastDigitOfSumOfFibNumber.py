def fib(n):
	last = ((1+5**0.5)/2)**n
	slast = ((1-5**0.5)/2)**n
	f = (last + slast)/(5**0.5)
	if(n<=1):
		return n
	else:
		return int(f+0.5)
n = int(input())
print(fib(n))