def pickingNumbers(a):
	l=[],maximum,count=0,0
    for i in a:
    	for j in a:
    		if(abs(i-j)<=1):
                count+=1
                l.append((i,j))
        l=[]
        if(maximum<count):
            maximum=count
        count=0
    return maximum

n = int(input())
a = list(map(int, input().split()))
print(pickingNumbers(a))
