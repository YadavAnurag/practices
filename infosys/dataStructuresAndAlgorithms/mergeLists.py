#DSA-Assgn-1
def merge_list(list1, list2):
    merged_data=""
    resultant_data = []
    for i in range(len(list1)):
    	if list1[i] is None:
    		resultant_data.append(list2[-(i+1)])
    	elif list2[-(i+1)] is None:
    		resultant_data.append(list1[i])
    	else:
    		resultant_data.append(list1[i]+list2[-(i+1)])
    return resultant_data

#Provide different values for the variables and test your program
list1=['The', 's', 'ris', 'in', None, 'ea']
list2=['st', 'the', None, 'es', 'un', None]
merged_data=merge_list(list1,list2)
print(*merged_data)