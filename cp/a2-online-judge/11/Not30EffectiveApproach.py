n = int(input())
lst = list(map(int, input().split()))
t = int(input())
elems = list(map(int, input().split()))


mylst = [(lst[i], i) for i in range(len(lst))]
mylst.sort(key=lambda x: x[0])

def binSearch(x, arr):
	low, high = 0, n
	while high>low:
		mid = (high-low)//2
		if arr[mid][0] == e:
			break
		elif arr[mid][0]>x:
			high = mid-1
		elif arr[mid][0]<x:
			low = mid+1
	return arr[mid][1]

rlst = mylst[::-1]

print(mylst, rlst)
vp, pp = 0,0
for e in elems:
	v = binSearch(e, mylst)
	p = binSearch(e, rlst)
	print('for ',e,v,'for ',e, p)
	vp += v
	pp += p 
print(vp, pp)












'''
TLE at 6th test

vp,pp=[],[]
for e in elems:
	v,p = 0,0
	for i in lst:
		if i==e:
			break
		v += 1
	for i in reversed(lst):
		if i==e:
			break
		p += 1
	vp.append(v+1)
	pp.append(p+1)
print(sum(vp),sum(pp))	
'''



