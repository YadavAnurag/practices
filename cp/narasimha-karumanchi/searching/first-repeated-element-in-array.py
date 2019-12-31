def solve(arr):
	d = {}
	for idx,elem in enumerate(arr):
		if elem in d:
			if d[elem]>0: d[elem] = -d[elem]
		else:
			d[elem] = idx+1
	high = -999999
	res = 999999
	for key,val in d.items():
		if val<0:
			new_high = max(high, val)
			if new_high>high: 
				res = key
				high = new_high
	return res

print(solve([2,6,1,3,3,3,2]))

