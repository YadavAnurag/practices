'''
	Filtering a list based on some condition
'''

ipt = [i for i in range(1000000)]
opt1 = []
opt2 = []


'''
	using if condition
	222 ms
'''
for i in ipt:
	if i%2==0: opt1.append(i)
print(opt1[:3])

'''
	using filter method
	234 ms
'''