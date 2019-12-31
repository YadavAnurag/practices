n = int(input())

high = 0
prev = 0
for _ in range(n):
	a,b = map(int, input().split())
	high = high-a+b
	if prev<high:
		prev = high
print(prev)