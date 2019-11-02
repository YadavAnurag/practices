def solve(arr):
	n = len(arr):
	d = {}
	for i in arr:
		d[i] += 1
	even, odd = 0,0
	for i in d.keys():
		if d[i]%2==0:
			even += 1
		else:
			odd += 1
	if even%2!=0:
		return even+odd-1
	else:
		return even+odd 
