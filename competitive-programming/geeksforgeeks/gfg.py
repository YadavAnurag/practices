for _ in range(int(input())):
    myString = input()
    count = 0
    for i in range(len(myString)-2):
        if 'gfg' == myString[i:i+3]:
            count += 1
    if count == 0:
        print(-1)
    else:
        print(count)