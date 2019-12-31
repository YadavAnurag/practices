def solve(elementList):
    i,j = 0, len(elementList)-1
    elementList.sort(reverse= False)

    while( i!=j ):
        if k > elementList[i]+elementList[j]:
            i += 1
        elif k < elementList[i]+elementList[j]:
            j -= 1
        elif k == elementList[i]+elementList[j]:
            return 'Yes' 

    return 'No' 



for _ in range(int(input())):
    n,k = map(int, input().split())
    elementList = list(map(int, input().split()))
    print(solve(elementList))
    


