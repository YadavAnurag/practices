y = int(input())
y += 1
flag = False
while not flag:
	ystr = str(y)
	if len(set(ystr)) == len(ystr): 
		flag=True 
	else:
		y += 1
print(y)
