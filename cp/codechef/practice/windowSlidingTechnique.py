'''Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array.'''

def solve(elements):
    import sys 
    maxSum = -sys.maxsize-1
    maxSum = max(maxSum, sum(elements[:k]))

    for i in range(1, len(elements)):
        if i+k-1 > len(elements)-1:
            return maxSum
        maxSum = max(maxSum, maxSum-elements[i-1]+elements[i+k-1])
    
    return maxSum



n = int(input())
elements = list(map(int, input().split()))
k = int(input())
print(solve(elements))


