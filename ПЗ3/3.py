def sum_list_a(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_list_a(arr[1:])
    
def sum_list_b(arr, f=None):
    if f is None:
        if any(x < 0 for x in arr):
            f = True
        else:
            raise ValueError("Список должен содержать отрицательные числа.")
    
    if not arr:
        return 0
    else:
        if arr[0] > 0:
            return arr[0] + sum_list_b(arr[1:], f)
        else:
            return sum_list_b(arr[1:], f)
        
print(sum_list_a([1, 2, 3, 4, 5]))
print(sum_list_b([1, -2, 3, -4, 5]))