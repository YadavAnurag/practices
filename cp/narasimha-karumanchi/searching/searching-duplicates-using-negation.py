def searching_duplicates_using_negation(arr):
	for i in range(len(arr)):
		print(arr)
		if arr[abs(arr[i])] < 0:
			return arr[i] 
		else:
			arr[abs(arr[i])] = -arr[abs(arr[i])]
	return -1

print(searching_duplicates_using_negation([3,1,1,6,2,4,5]))

