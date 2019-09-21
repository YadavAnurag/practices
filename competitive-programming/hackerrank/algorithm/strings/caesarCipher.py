n = int(input())
s = input()
k = int(input())

new = ''
for i in s:
	if i.isalpha():
		if i.isupper():
			new += chr(65+(ord(i)+k-65)%26)
		if i.islower():
			new += chr(97+(ord(i)+k-97)%26)
	else:
		new += i
print(new)