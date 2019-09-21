for _ in range(int(input())):
    n,m = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    result = []
    i,j = 0,0
    while not (i==n and j==m):
        if i==n:
            result += second[j:]
            break
        if j==m:
            result += first[i:]
            break
        if first[i]<=second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    print(*result)

