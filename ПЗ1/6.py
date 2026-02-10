arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

def bin_search(arr, n):
    c = 0
    left, right = 0, len(arr)-1
    while left < right:
        c += 1
        middle = (left + right) // 2
        if arr[middle] < n:
            left = middle + 1
        else:
            right = middle
        print(arr[left:right+1])
    return (left, c)
    
def lin_search(arr, n):
    c = 0
    for i in range(len(arr)):
        c += 1
        print(i)
        if arr[i] == n:
            return (i, c)


print(lin_search(arr, 1))
print(bin_search(arr, 1))