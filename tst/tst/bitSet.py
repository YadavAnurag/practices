import math
def upto(a,b):
	pair = n//(num)

	if(k==1):
		tor = math.ceil(pair/2)
	else:
		tor = math.floor(pair/2)*num

	rem = n%num
	if(rem):
		if((n-rem)&num != num):
			tor+=rem


for j in range(int(input())):

	s = int(input())
	m,n,k = map(int, input().split())
	num = 2**(k-1)
	count=0

	pair = n//(num)
	
	if(k==1):
		tor = math.ceil(pair/2)
	else:
		tor = math.floor(pair/2)*num

	rem = n%num
	if(rem):
		if((n-rem)&num != num):
			tor+=rem
	

	

	spair = m//num
	
	if(k==1):
		tol = math.ceil(spair/2)
	else:
		tol = math.floor(spair/2)*num

	rem = m%num
	if(rem):
		if((m-rem)&num != num):
			tol+=rem

	

	total = tor+tol


	
	


	for i in range(m,n+1):
		if(i&num==num):
			count+=1

	print(count)
	
