for _ in range(int(input())):
    q = int(input())
    n = int(input())
    elementList = list(map(int, input().split()))
    

    posOne = -1
    for i, elem in enumerate(elementList):
        if elem == 1:
            posOne = i
    
    for i, ele