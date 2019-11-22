def isPalindrome(A):
    if A<0:
        return False
    a = str(A)
    i = 0
    while i<len(a)//2:
        if a[i] != a[-(i+1)]:
            return False
        i += 1
    return True

print(isPalindrome(2147447412))