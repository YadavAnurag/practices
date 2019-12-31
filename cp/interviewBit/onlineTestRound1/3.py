def solve(arr1, arr2):
	arr1.sort(reverse=True)
	arr1.sort(reverse=True)

	count = 0
	n1,n2 = len(arr1), len(arr2)
	i,j = 0,0
	while True:
		if i>=n1 or j>=n2:
			break
		if arr2[j]<=arr1[i]:
			count += arr2[j]
			i += 1
		j += 1
	return count