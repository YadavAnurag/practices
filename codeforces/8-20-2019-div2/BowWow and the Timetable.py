binaryInput = input()
decimalInput = int('0b'+binaryInput, 2)

i=0
counter = 0
while 4**i < decimalInput:
	counter += 1
	i += 1
print(counter)