first = input()
second = input()
third = input()

fd,sd,td = {},{},{}

for i in range(26):
	fd[chr(65+i)] = 0
	sd[chr(65+i)] = 0
	td[chr(65+i)] = 0

for char in first:
	fd[char] += 1
for char in second:
	sd[char] += 1
for char in third:
	td[char] += 1

flag = 1
i = 0
while i<26 and flag==1:
	if td[chr(65+i)] != (fd[chr(65+i)]+sd[chr(65+i)]):
		flag = 0
	i += 1

print('YES') if flag else print('NO')