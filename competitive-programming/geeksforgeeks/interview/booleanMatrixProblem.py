for _ in range(int(input())):
    n,m = map(int, input().split())
    elements = []


    for i in range(n):
        elements.append(list(map(int, input().split())))

    setx = set()
    sety = set()

    for i in range(n):
        for j in range(m):
            if elements[i][j] == 1:
                setx.add(i)
                sety.add(j)

    for i in range(n):
        for j in range(m):
            if (i in setx) or (j in sety):
                elements[i][j] = 1
    
    for i in range(n):
        print(*elements[i])