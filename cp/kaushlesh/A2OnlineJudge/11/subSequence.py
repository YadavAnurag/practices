1.
def subSequence(a, b):
	i,j = 0,0
	m,n = len(a),len(b)
	while i<m and j<n:
		if a[i]==b[j]:
			i += 1
		j += 1
	return i==m
#print(solve('ag', 'anurag'))


2.
def matrix(N, operations):
	ROW = [0]*N
	COL = [0]*N
	for char, i, x  in operations:
		if char=='c':
			COL[i] += x
		if char=='r':
			ROW[i] += x 
	return(max(COL)+max(ROW))
#print(solve1(3, [('r',0,3),('c',1,5),('r',0,5),('r',0,1)]))


3.
def sumOfX(n):
	digitSum = lambda x: sum(map(int, str(x)))

	count = 0
	for x in range(n-97, n+1):
		if n == (x + digitSum(x) + digitSum(digitSum(x))):
			count += 1
	return count
print(sumOfX(999999999))

4.
import math
numOfBits = lambda num,base: math.floor(math.log(num,base)+1)
#print(numOfBits(4,2))


5.
def equalToffee(arr):
	return sum(arr)-min(arr)*len(arr)
print(equalToffee([1,8,3]))
