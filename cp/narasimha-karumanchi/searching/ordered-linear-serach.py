def ordered_linear_serach(arr, x):
	for i in range(0, len(arr), 2):
		if arr[i]==x:
			return i 
		elif arr[i]>x:
			if arr[i-1]==x:
				return i-1
			else:
				return -1
	return -1

print(ordered_linear_serach([3,4,5,7,9], 11))