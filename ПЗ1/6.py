arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

def bin_search(arr, n):
    left, right = 0, len(arr)-1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < n:
            left = middle + 1
        else:
            right = middle
        print(arr[left:right+1])
    return left

def lin_search(arr, n):
    for i in range(len(arr)):
        print(i)
        if arr[i] == n:
            return i


print(lin_search(arr, 1))
print(bin_search(arr, 1))