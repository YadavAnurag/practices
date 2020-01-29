n,q = map(int, input().split())
arr = list(map(int, input().split()))
t,l,r,a,b,value,index = 0,0,0,0,0,0,0

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

for i in range(q):
    inputList = list(map(int, input().split()))
    if inputList[0]==2:
        _,l,r,a,b =inputList
        if gcd(a,b)==1:
            print(0)
            continue
        
        g,ans = gcd(a,b),0
        for j in range(l-1,r):
            ans += min(arr[j]%g, g-arr[j]%g)
        print(ans)
    else:
        arr[inputList[1]-1] = value 
