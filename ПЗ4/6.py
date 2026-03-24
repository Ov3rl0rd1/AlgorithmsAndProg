arr = [-5, -3, -1, 0, 2, 4, 6]

def sort_by_absolute(arr):
    left = 0
    right = len(arr)-1
    
    result = []
    
    while left <= right:
        if abs(arr[left]) < abs(arr[right]):
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right -= 1
    
    return result

sorted_arr = sort_by_absolute(arr)
print(sorted_arr)