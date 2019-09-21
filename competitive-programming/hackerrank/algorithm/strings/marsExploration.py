s = input()

expected = 'SOS'*(len(s)//3)
count=0
for i in range(len(s)):

	if s[i]!=expected[i]:
		count+=1
print(count)
