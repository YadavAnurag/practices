def searching_first_duplicate_using_hash(arr):
	dictionary = dict()

	for i in range(len(arr)):
		if arr[i] not in dictionary:
			dictionary[arr[i]] = 1
		else: dictionary[arr[i]] += 1
		if dictionary[arr[i]] == 2:
			return arr[i]
	return -1

print(searching_first_duplicate_using_hash([1,2,9,3,4,5]))