vowel = 'aeiouAEIOU'

while True:
	s = input()
	if s is '0':
		break
	slist = list(s.split())

	for i in range(len(slist)):
		if slist[i][0] not in vowel:
			slist[i] = 'T'+slist[i][1:].lower()
		else:
			slist[i] = 'T'+slist[i].lower()

	string = ' '.join(slist)	
	print(string)
