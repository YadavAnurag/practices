n = int(input())
elements = list(map(int, input().split()))

newList = [0]
temp = 0
for i in elements:
  temp = i
  if temp<i:
    newList.append(0)
  else:
    newList.append(1)
print(newList)
count = 0
prev = newList[0]
for i in range(len(newList)):
  if newList[i] == 0:
    prev = 0
  if newList[i] == 1:
    if prev == 1:
      count += 1
    prev = 1
print(count)