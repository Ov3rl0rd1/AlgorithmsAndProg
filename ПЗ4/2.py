def count_elements(arr):
    if not arr:
        return 0
    else:
        return 1 + count_elements(arr[1:])
    
arr = [1, 2, 3, 4, 5]
print(count_elements(arr))