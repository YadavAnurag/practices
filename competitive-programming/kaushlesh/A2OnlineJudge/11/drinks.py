n = int(input())
elems = list(map(int, input().split()))

p = 0
for i in elems:
	if i!=0:
		p += i/100
res = p/(n)*100
print(f'{res:.4f}')