
def check_double(list1, list2):
	total = []
	for i in list1:
		if i*2 in list2:
			total.append(i)
	return total

list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))