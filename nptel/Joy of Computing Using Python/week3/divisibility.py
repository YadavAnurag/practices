# numList = list(range(1, 51))
# num = int(input())
# count = 0
# for item in numList:
# 	if(item%num==0 and item!=num):
# 		count = count+1
# print(count)

for i in range(11,16):
	if i%2==0:
		print('Jack')
	elif i%3==0:
		print('Jill')
	elif i%2==0 and i%3==0:
		print('Jack and Jill')
	else:
		print('Jill and Jack')