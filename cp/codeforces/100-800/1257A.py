def solve(arr):
    n,x,a,b = arr

    if a>b:
        a,b = b,a

    if abs(a-b)==n-1: return abs(a-b)
    g1 = abs(1-a)
    g2 = abs(n-b)
    if x>(g1+g2): 
        return n-1
    else:
        return abs(a-b)+x
    


for _ in range(int(input())):
    arr = map(int, input().split())
    print(solve(arr))