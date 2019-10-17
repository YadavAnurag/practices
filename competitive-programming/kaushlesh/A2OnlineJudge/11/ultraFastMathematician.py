a = input()
b = input()

res = ''
for i,j in zip(a,b):
	res += str(int(i)^int(j))

print(res)