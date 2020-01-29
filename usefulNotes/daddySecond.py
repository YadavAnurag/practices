mat = []
n,m = map(int, input().split())

for i in range(n):
    mat.append(list(map(int, input().split())))

prev = -1
for row in mat:
    for elem in row:
        if elem == 0:
            prev = -1
        else: 
            if prev == -1:
                try:
                    pass
                except Exception as e:
                    raise e
                
                    
