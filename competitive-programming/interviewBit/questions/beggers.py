def solve(A, B):
    arr = [0 for _ in range(A)]
    
    for i in range(len(B)):
        arr[B[i][0]-1] += B[i][2]
        try:
            arr[B[i][1]+1-1] -= B[i][2]
        except IndexError:
            pass
    for i in range(1, A):
        arr[i] = arr[i-1] + arr[i]
    return arr


A = 5
B = [
  [1, 2, 10],
  [2, 3, 20],
  [2, 5, 25]
]
print(solve(A, B))