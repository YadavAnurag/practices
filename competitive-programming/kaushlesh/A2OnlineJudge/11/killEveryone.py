n = int(input())

f = [i+1 for i in range(n)]

i=0
while len(f)>2:
	print('remove',f[(i+2)%len(f)])
	del f[(i+2)%len(f)]
	i += 1
	if i>len(f):
		i = i%len(f)
		print(i,'i')
	print(f)
# print(f)