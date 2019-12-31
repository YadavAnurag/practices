for _ in range(int(input())):
    size = int(input())
    elements = list(map(int, input().split()))

    setElements = set(elements)

    if len(setElements) < len(elements):
        print('Yes')
    else:
        print('No')