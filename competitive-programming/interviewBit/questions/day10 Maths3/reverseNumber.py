def reverse(A):
    flag = False
    if A<0:
        n = 0 - A
        flag = True
    else:
        n = A
    ans,r = 0,0
    while n!=0:
        r = n%10
        ans = ans*10 + r
        n = n//10
    if flag:
        ans = 0 - ans
    if ans<=-2**31 or ans>=2**32-1:
        return 0
    return ans

print(reverse(-1146467285))