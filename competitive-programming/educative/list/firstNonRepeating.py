lst = [4, 5, 1, 2, 0, 4]

def findFistUnique(lst):
	counts = dict().fromkeys(lst,0)
	for i in lst:
		counts[i]+=1

	for i in lst:
		if counts[i]==1:
			return i
	return None


print(findFistUnique(lst))
