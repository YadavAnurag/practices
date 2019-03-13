def intreverse(n):
	ans = 0
	while(n!=0):
		ans = ans*10 + n%10
		n = int(n/10)
	return ans
print(intreverse(798798))

def matched(n):
	a = 0
	for i in n:
		if(a<0):
			return False
		if(i=='('):
			a = a+1
		if(i==')'):
			a = a-1
	if(a==0):
		return True
	if(a!=0):
		return False
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))

#Sumprimes
def primes(n):
	if(n<=1):
		return False
	for i in range(2, int(pow(n, 1/2))+1):
		if(n%i==0):
			return False
	return True
def sumprimes(l):
	sum = 0
	for i in l:
		if(primes(i) and i>0):
			sum = sum + i
	return sum

print(sumprimes([17,51,29,39]))
print(sumprimes([-3,-5,3,5]))
print(sumprimes([4,6,15,27]))
