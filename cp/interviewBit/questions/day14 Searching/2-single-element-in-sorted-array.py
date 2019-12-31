def single_element_in_sorted_array(A):
	x = 0
	for i in A: x ^= i
    return x

print(single_element_in_sorted_array([1,1,5,5,3]))