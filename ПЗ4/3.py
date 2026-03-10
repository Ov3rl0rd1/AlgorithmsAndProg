def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        max_of_rest = find_max(arr[1:])
        return max(arr[0], max_of_rest)
    
arr = [3, 1, 4, 1, 5, 9]
print(find_max(arr))