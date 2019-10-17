n = int(input())
s = input()

prev = ''
count = 0

for i in s:
	if i==prev:
		count += 1
	prev = i
print(count)