n = int(input())
deg = list(map(int, input().split()))

if sum(deg)==2*(n-1):
	print("Yes")
else:
	print('No')