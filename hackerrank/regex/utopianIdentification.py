import re
for _ in range(int(input())):
	print('VALID' if bool(re.match(r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$',input().strip())) else 'INVALID')