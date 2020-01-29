s = input()
count,other = 0,0
for i in s:
    if i=='a':
        count += 1
    else: 
        other += 1
if count>other:
    print(len(s))
else:
    while count<=other:
        other -= 1
    print(other+count)