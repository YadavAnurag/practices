n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sum = 0
prev = b[0]
for i in range(0, len(a)):
	if i == 0:
		sum += b[a[i]-1]
		prev = a[i]
	else:
		if (a[i] == prev+1):
			sum += b[a[i]-1]
			sum += c[a[i]-2]
			prev = a[i]
		else:
			sum += b[a[i]-1]
			prev = a[i]

print(sum)