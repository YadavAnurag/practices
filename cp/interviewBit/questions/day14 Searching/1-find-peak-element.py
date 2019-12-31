def find_peak_element(A):
	if len(A)==1: return A[0]
	if A[0]>=A[1]: return A[0]
	if A[-1]>=A[-2]: return A[-1]

	for i in range(1, len(A)-1):
		if A[i]>=A[i-1] and A[i]>=A[i+1]: return A[i]

print(find_peak_element([10, 25, 20, 11]))
