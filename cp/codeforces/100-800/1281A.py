def solve(string):
    s = string
    f,j,k = 'FILIPINO','JAPANESE','KOREAN'

    if len(s)>=5:
        if s[-5:] == 'mnida': return k 
    if len(s)>=4:
        if s[-4:]=='desu' or s[-4:]=='masu': return j 
    if len(s)>=2:
        if s[-2:]=='po': return f 

for _ in range(int(input())):
    s = input()
    print(solve(s))