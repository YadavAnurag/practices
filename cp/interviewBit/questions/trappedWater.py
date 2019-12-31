def trap(A):
        leftA, rightA = [0]*len(A),[0]*len(A)
        
        temp = 0
        for i in range(len(A)):
            if A[i]>temp:
                leftA[i] = A[i]
                temp = A[i]
            else:
                leftA[i] = temp
        temp = 0
        for i in range(len(A)-1, -1, -1):
            if A[i]>temp:
                rightA[i] = A[i]
                temp = A[i]
            else:
                rightA[i] = temp
        
        count = 0
        print(A, leftA, rightA)
        for i in range(1, len(A)-1):
            count += (min(leftA[i], rightA[i])-A[i])
        return count
print(trap([ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]))
