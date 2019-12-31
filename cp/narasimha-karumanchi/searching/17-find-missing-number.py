def find_missing_number(arr):
	x = 0
	# for i in arr:
	# 	x ^= i 
	# for i in range(1, len(arr)+2):
	# 	x ^= i 
	# return x
	for idx,val in enumerate(arr, 1):
		x ^= (idx^val)
	return x^(len(arr)+1)

print(find_missing_number([8,2,3,1,4,5,6]))
