k = int(input())
b = list(map(int, input().split()))
a = [b[0]]+b
for i in range(len(b)):
	if (a[i]<=b[i]):
		pass
	else:
		a[i] = b[i]
print(sum(a))