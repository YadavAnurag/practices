n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

minimum = min(c)-min(a)
maximum = max(c)-max(a)

print(*[i for i in range(minimum, maximum+1)])
