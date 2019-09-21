from collections import Counter
n = int(input())
a = list(map(int, input().split()))
d = Counter(a)
sum=0
for i in d:
	sum += d[i]//2
print(sum)

