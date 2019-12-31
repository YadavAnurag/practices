n = int(input())
dishes = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

point = 0
prev = 0
for index, dish in enumerate(dishes):
	if index==0:
		point += b[dish-1]
	else:
		if prev+1 == dish:
			point += (b[dish-1]+c[prev-1])
		else:
		 	point += b[dish-1]
	prev = dish

print(point)