lst = [4, 2, 1, 5, 0]


def findSecondMaximum(lst):
	shigh,high=min(lst),min(lst)
	for i in lst:
		print('For ',i)
		if i > high:
			shigh = high
			high = i
		else:
			if i>shigh:
				shigh = i
		print(high,shigh)
	return shigh 

print(findSecondHigh(lst))