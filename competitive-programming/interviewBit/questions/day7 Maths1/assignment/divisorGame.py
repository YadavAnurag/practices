def solve(A, B, C):
    if B>C:
        b,c = B,C
    else:
        b,c = C,B
    while c:
        b,c = c, b%c
    
    lcm = B*C//(b)
    
    count = 0
    i = 1
    while lcm<=A:
        if lcm%B==0 and lcm%C==0:
            count += 1
            print(count)
        lcm *= i
    
            
    return count


#     temp = B*C
#     count = 0
#     while temp<=A:
#         if temp%B==0 and temp%C==0:
#             count += 1
#             print(temp)

#         if temp+B<temp+C:
#             temp += B
#         else:
#             temp += C
        
#     return count
print(solve(81991,2549,7))