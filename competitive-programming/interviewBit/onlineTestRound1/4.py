t=int(input())
i=0
while (i<t):
	n=int(input())
	a=list(map(int,input().split()))
	j=1
	leftend=0
	while(j<n and a[j]>a[j-1]):
		leftend+=1
		j+=1
	rightend=n-1
	j=n-2
	while(j>=0 and a[j]<a[j+1]):
		j-=1
		rightend-=1
	if(n==1):
		print(0)
	else:
		if(rightend==0 and leftend==n-1):
			print(int(n*(n-1)/2+n-1))
		else:
			k=0
			s=0
			while(k<=leftend):

				l=rightend
				posi=0
				notFound=True
				while(l<n and notFound):
					if(a[l]>a[k]):
						posi=l
						notFound=False
					l+=1
				if(notFound):
					s+=(n-l+1)
				if(not notFound):
					s+=(n-posi+1)
				k+=1
			s+=n-rightend
			print(s)
				
	i+=1