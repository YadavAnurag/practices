s = input()

up, low = 0,0
for i in s:
	if i.isupper():
		up += 1  
	else:
		low += 1

print(s.lower()) if(low>up) else(print(s.lower()) if low==up else print(s.upper()))