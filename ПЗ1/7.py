arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 4, 4, 6, 6]

def first_x(arr, x):
    left, right = 0, len(arr)-1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < x:
            left = middle + 1
        else:
            right = middle
    return left

def last_x(arr, x):
    left, right = 0, len(arr)-1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] <= x:
            left = middle + 1
        else:
            right = middle
    return left - 1


def count_x(arr, x):
    first = first_x(arr, x)
    if first == -1:
        return 0
    last = last_x(arr, x)
    return last - first + 1

def first_even(arr):
    left, right = 0, len(arr)-1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] % 2 != 0:
            left = middle + 1
        else:
            right = middle
    return left


print(first_x(arr, 1))
print(last_x(arr, 1))
print(count_x(arr, 1))
print(first_even(arr))