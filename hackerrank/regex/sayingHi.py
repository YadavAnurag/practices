import re 

for _ in range(int(input())):
    s = input()
    if bool(re.match(r'^[Hh]{1}[Ii]{1}\s{1}[^Dd]{1}\w*', s)):
    	print(s)
