def solve(A):
    currMax = A[0]
    allMax = A[0]
    
    for i in range(1,len(A)):
        currMax = max(A[i], currMax+A[i])
        allMax = max(currMax, allMax)
    return allMax
print(solve([1,2,3,4,-10]))