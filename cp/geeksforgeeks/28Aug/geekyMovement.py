for _ in range(int(input())):
	n = int(input())
	myList = list(map(int, input().split()))

	count = 0
	for i in range(0,len(myList)-3,2):

		diff = max(abs(myList[i]-myList[i+2]),abs(myList[i+1]-myList[i+3]))
		count += diff
	print(count)
