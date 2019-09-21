def trappingWater(arr, n):
	sum = 0
	for i in range(1,len(arr)-1):
		temp = arr[0]-arr[i]
		if (temp)>=0:
			sum += temp
	return sum

for _ in range(int(input())):
	n = int(input())
	mylist = list(map(int, input().split()))
	print(trappingWater(mylist, n))

