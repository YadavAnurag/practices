import math 

a, b = map(int, input().split())

factors = []
for i in range(2, math.ceil(min(a,b)**0.5)):
	if a%i==0 and b%i==0: 
		factors.append(i)
		if b%(a//i)==0: factors.append(a//i)
print(factors)

factors.sort()
for i in range(len(factors)):
	power = 2
	if factors[i]:
		temp = factors[i]
		for j in range(len(factors)):
			if factors[j]:
				if factors[j]!=factors[i]:
					if temp%factors[j]==0:
						factors[j] = False
					temp *= power
					power += 1

count = 0
for i in factors:
	if i: count += 1

def nCr(n, r): 
    return (fact(n) / (fact(r)* fact(n - r))) 
def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i     
    return res

# print(int(nCr(count+1, 2)))
# print(count+1)

