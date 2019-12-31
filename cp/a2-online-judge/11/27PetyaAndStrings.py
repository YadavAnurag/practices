a = input().lower()
b = input().lower()

for i,j in zip(a,b):
	if i<j:
		print(-1)
		break
	if i>j:
		print(1)
		break
else:
	print(0)