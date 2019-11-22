def solve(A):
    print('next')
    arr = []
    pos = 0
    maxPos = 0
    for i in range(len(A)):
        if A[i] < 0:
            pos = 0
            arr.append(-1)
        else:
            pos += 1
            arr.append(pos)
        maxPos = max(pos, maxPos)
    
    i = 0
    first = 0
    while arr[i]!=maxPos:
        if arr[i]<0:
            first = 0
        else:
            first += 1
        print(arr[i], first)
        i += 1
    print(A[i], first)

    return A[i-first:i+1]

print(solve([5,6,-1, 7, 8,9,-5, 2,3,4,5, -1, 2,3,4,6,6, 3]))
print(solve([1,2,3,5,-1,6,2, 5]))
print(solve([79, 40, -83, -14, -81, 64, -60, -75, -95, 73]))
print(solve([33, -73, 52, -17, 76, -32, 46, 99, -12, -21]))