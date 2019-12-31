k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
elems = [k,l,m,n]
dragons = [i+1 for i in range(d)]

i = 0
def suffered(elems,dragons,d):
	if min(k,l,m,n)==1:
		return d
	else:
		high = dragons[-1]
		for elem in elems:
			i = 1
			while elem*i<=high and i<len(dragons):
				dragons[elem*i-1] = False
				i += 1
		count = 0
		for i in dragons:
			if i:
				count += 1

	return d-count



print(suffered(elems, dragons, d))