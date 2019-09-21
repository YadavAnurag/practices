n = int(input())
s = input()

d = {'o': 0, 'n': 0, 'e':0, 'z':0, 'r':0}
for c in s:
	if c is 'o':
		d['o'] += 1
	elif c is 'n':
		d['n'] += 1
	elif c is 'e':
		d['e'] += 1
	elif c is 'z':
		d['z'] += 1
	elif c is 'r':
		d['r'] += 1

ones = min(d['o'], d['n'], d['e'])
d['o'] = d['o']-ones
d['n'] = d['n']-ones
d['e'] = d['e']-ones

zeros = min(d['z'], d['e'], d['r'], d['o'])

total = [1]*ones + [0]*zeros
print(*total)