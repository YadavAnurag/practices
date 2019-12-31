def interpolation_search(arr, x):
	low = 0
	high = len(arr)-1

	while arr[low]<=x and arr[high]>=x:
		mid = (low+((x-arr[low])*(high-low))//(arr[high]-arr[low]))

		if arr[mid]<x: low=mid+1
		elif arr[mid]>x: high=mid-1
		else: return mid
	if arr[low]==x:
		return low  
	return -1

print(interpolation_search([1,2,3,4,5,19], 19))