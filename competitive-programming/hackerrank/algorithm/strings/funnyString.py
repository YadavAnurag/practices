for _ in range(int(input())):
	s = input()

	funny = True
	for i in range(len(s)-1):
		if abs(ord(s[i])-ord(s[i+1]))==abs(ord(s[-i-1])-ord(s[-i-2])):
			pass
		else:
			funny = False
			break
	print('Funny' if funny else 'Not Funny')