a,b,n = map(int, input().split())

val = a
for _ in range(n):
	for i in range(10):
		x = val*10+i 
		if x%b==0:
			val = x
			break
print(-1) if val==a else print(val)
