volwel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(int(input())):
	count=0
	string = input()
	for j in string:
		if j in volwel:
			count+=1
	print(count)

