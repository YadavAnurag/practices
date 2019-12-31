def bin_serach_recursive(arr, x, low=0, high=-1):
	if not arr: return -1
	if high==-1: high = len(arr)-1
	if low==high:
		if arr[low]==x: return low
		else: return -1
	mid = low+(high-low)//2
	if arr[mid]>x: return bin_serach_recursive(arr, x, low, mid-1)
	elif arr[mid]<x: return bin_serach_recursive(arr, x, mid+1, high)
	else: return mid 

print(bin_serach_recursive([1,2,3,4,5,8], 4))
