for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split()))

    result = []
    myDict = dict([(0,0), (1,0), (2,0)])
    print(myDict, elements, myDict[0], myDict[1], myDict[2])
    for i in elements:
        if i == 0:
            myDict[0]+=1
        elif i == 1:
            myDict[1]+=1
        elif i == 2:
            myDict[2]+=1
    print(myDict, elements, myDict[0], myDict[1], myDict[2])
    result += [0]*myDict[0]
    result += [1]*myDict[1]
    result += [2]*myDict[2]

    print(result)

