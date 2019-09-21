for _ in range(int(input())):
    n,k = map(int, input().split())
    elements = list(map(int, input().split()))

    prevSum = 0
    currentSum = 0
    
    for i in range(1,len(elements)):
        if prevSum == k:
            print(0+1,0+1)
            break
        
        currentSum = prevSum + elements[i]
        if currentSum > k:
            currentSum -= elements[i]
