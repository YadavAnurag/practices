def solve(tup):
    a,b = tup
    res = 0
    n = abs(a-b)
    p = 0
    while 5**p<=n:
        if p == 0:
            if 5**(p+1)<=n:
                p *= 2
            else:
                n %= 5
                res += p
        else:
            if 5**(p*2)<=n:
                p *= 2
            else:
                n %= 5
                res += p
    temp = res*5 
    while temp<n:
        temp += 5
        res += 1

    return res

for _ in range(int(input())):
    tup = map(int, input().split())
    print(solve(tup))