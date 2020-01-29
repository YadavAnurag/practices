def solve(h,m):
    mintues = 0
    if h==23:
        if m==0: 
            return 60
        else:
            mintues += (60-m)
    else:
        if m==0:
            mintues += (24-h)*60 
            return mintues
        else:
            mintues += (23-h)*60
            mintues += (60-m)

    return mintues

for _ in range(int(input())):
    h,m = map(int, input().split())
    print(solve(h,m))

