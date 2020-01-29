for _ in range(int(input())):
    n,k1,k2 = map(int, input().split())

    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    l1.sort()
    l2.sort()


    while True:
        if l1==[] or l2==[]: break
        a,b = l1.pop(), l2.pop()
        if a>b: 
            l1.extend([a,b])
        else:
            l2.extend([a,b])
    if l1==[]: print('NO')
    else: print('YES')