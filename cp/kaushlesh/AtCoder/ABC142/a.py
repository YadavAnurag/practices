n = int(input())
x = 1 if n==1 else((n//2+1)/n if n%2!=0 else 0.5)
print(x)
