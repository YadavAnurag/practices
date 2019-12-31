def binary_search(elements, target):
    low = 0
    high = len(elements)-1

    while low <= high:
        mid = low + (high-low)//2

        if elements[mid] == target:
            return elements[mid]
        elif elements[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return 'Element Not Found'


print(binary_search([1, 2, 3, 4, 5, 6], 41))
