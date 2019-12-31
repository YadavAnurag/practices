# def ternarySearch(low, high, key):
# 	mid1 = low + (high-low)/3
# 	mid2 = high - (high-low)/3
# 	if(high>=low):
# 		if(myList[mid1]==key):
# 			return mid1
# 		elif(myList[mid2]==key):
# 			return mid2
# 		elif(myList[mid1]>key):
# 			return ternarySearch(low, mid1-1, key)
# 		elif(myList[mid2]<key):
# 			return ternarySearch(mid2+1, high, key)
# 		else:
# 			return ternarySearch(mid1+1, mid2-1, key)
# 	return -1

def unimodel(x):
	return 2*(x**2)-12*x+7

def minOfUnimodel(low, high):
	for i in range(0, 200):
		mid1 = (2*low+high)/3
		mid2 = (low+2*high)/3
		if(unimodel(mid1)>unimodel(mid2)):
			low = mid1
		else:
			high = mid2
	return unimodel(low)

n = int(input())
for i in range(0, n):
	(a, b) = map(int, input().split())
	ans = minOfUnimodel(a, b)
	if(ans<0):
		print(int(ans)-1)
	else:
		print(int(ans))
