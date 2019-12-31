def bin_search(arr, x):
	n = len(arr)
	low, high = 0, n-1

	while low<=high:
		mid = low+ (high-low)//2

		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			high = mid - 1
		else:
			low = mid + 1
	return -1

print(bin_search([1,2,3,4,5,6,7], 9))