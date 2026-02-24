def count_odd_iterative(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count

def count_odd_recursive(arr):
    if not arr:
        return 0
    else:
        if arr[0] % 2 != 0:
            return 1 + count_odd_recursive(arr[1:])
        else:
            return count_odd_recursive(arr[1:])
        
print(count_odd_iterative([1, 2, 3, 4, 5]))
print(count_odd_recursive([1, 2, 3, 4, 5]))
        
# Стек вызовов для count_odd_recursive([1, 2, 3, 4, 5]):
# count_odd_recursive([1, 2, 3, 4, 5]) -> 1 + count_odd_recursive([2, 3, 4, 5])
# count_odd_recursive([2, 3, 4, 5]) -> count_odd_recursive([3, 4, 5])
# count_odd_recursive([3, 4, 5]) -> 1 + count_odd_recursive([4, 5])
# count_odd_recursive([4, 5]) -> count_odd_recursive([5])
# count_odd_recursive([5]) -> 1 + count_odd_recursive([])
# count_odd_recursive([]) -> 0