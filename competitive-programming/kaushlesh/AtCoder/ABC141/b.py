s = input()



def yesNo(s):
	for index, char in enumerate(s):
		if index%2==0:
			if char=='L':
				return 'No'
		else:
			if char=='R':
				return 'No'
	return 'Yes'

print(yesNo(s))
