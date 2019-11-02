count = 0
for _ in range(int(input())):
	op = input()
	if op=='++X' or op=='X++':
		count += 1
	else:
		count -= 1
print(count)