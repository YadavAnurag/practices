# def solve(A):
# 	flag = 0
# 	z = 0
# 	for i in range(len(A)-1, 0, -1):

# 		if A[i-1] < A[i]:
# 			flag = 1
# 			z = i
# 			break
# 	k = A[z-1]
# 	ans = k
# 	temp = 10**6
# 	s = -1
# 	for j in range(z,len(A[z:len(A)])+1):
# 		if (((A[j]-A[z-1]) < temp) and (A[j]-A[z-1])>0):
# 			temp = A[j]-k
# 			ans = A[j]
# 			s = j

# 	A[z-1],A[s] = A[s],A[z-1]


# 	if flag==1:
# 		return A
# 	else:
# 		A.reverse()
# 		return A
# print(solve([1,2,3]))

def solve(A):
	n = len(A)  
	for i in range(n-1,0,-1): 
		if A[i] > A[i-1]: 
			break
	x = A[i-1] 
	low = i 
	for j in range(i+1,n): 
		if A[j] > x and A[j] < A[low]: 
			low = j 
		
	A[low],A[i-1] = A[i-1], A[low] 
	arr = A[:i]
	return arr+sorted(A[i:])

print(solve([3,7,6,5]))