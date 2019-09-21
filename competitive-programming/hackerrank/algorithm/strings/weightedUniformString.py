s = input()
queries = []
for _ in range(int(input())):
	queries.append(int(input()))


weights = set()
i=0
while(True):
	if i==len(s):
		break
	a = s[i]
	w = 0
	while(s[i]==a):
		w += ord(s[i])-96
		weights.append(w)
		i += 1
		if i==len(s):
			break


print(["Yes" if i in weights else "No" for i in queries])

