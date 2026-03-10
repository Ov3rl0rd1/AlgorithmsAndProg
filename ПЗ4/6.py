arr = [-5, -3, -1, 0, 2, 4, 6]

def sort_by_absolute(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort_by_absolute(arr[:mid])
    right = sort_by_absolute(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if abs(left[i]) < abs(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

sorted_arr = sort_by_absolute(arr)
print(sorted_arr)