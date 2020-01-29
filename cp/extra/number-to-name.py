d = {
0: 'Zero',
1: 'One',
2: 'Two',
3: 'Three',
4: 'Four', 
5: 'Five', 
6: 'Six', 
7: 'Seven', 
8: 'Eight', 
9: 'Nine'}
inp = int(input())
s = ''

rem = 0
while(inp!=0):
    rem = inp%10
    s = (d[rem]+' ') + s
    inp = inp//10

print(s)