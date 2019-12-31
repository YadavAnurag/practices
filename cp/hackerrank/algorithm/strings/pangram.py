s = input()
s = s.lower()
s = s.replace(' ','')
a = list(set(s))
print(s,sorted(a),len(set(s)))
if len(set(s))>=26:
	print('pangram')
else:
	print('not pangram')