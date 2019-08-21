n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = a+b


def solve(a, b):
    for i in a:
        for j in b:
            if i+j not in c:
                return i, j


print(*solve(a, b))
