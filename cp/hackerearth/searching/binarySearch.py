n = int(input())
myList = list(map(int, input().split(' ')))
myList.sort(reverse = False)
m = int(input())

def binSearch(high, low, key):
	while(low<=high):
		mid = int((low+high)/2)
		# print('mid', mid)
		if(myList[mid]<key):
			low = mid+1
			# print('high', high)
		elif(myList[mid]>key):
			high = mid-1
			# print('low', low)
		else:
			return mid+1
	return -1

for i in range(0, m):
	q = int(input())
	print(binSearch(n-1, 0, q))