import re
for _ in range(int(input())):
	s = input()
	print('YES' if bool(re.match(r'[A-Z]{5}\d{4}[A-Z]', s)) else 'NO')