# mylist = list(map(int, input().split()))
# s = int(input()) 


def find_array_quadruplet(arr, s):
	for i in range(len(arr)-4):
		if s == sum(arr[i:i+4]):
			elem = arr[i:i+4]
			elem.sort()
			return elem
	return []

print(find_array_quadruplet([2, 3, 4, 0, 9, 5, 1, 3, 4], 20))