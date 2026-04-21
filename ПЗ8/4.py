#Задача № 4
#Реализуйте алгоритм сортировки подсчетом.

def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    
    if min_val < 0:
        shift = -min_val
        max_val += shift
        range_size = max_val + 1
    else:
        shift = 0
        range_size = max_val + 1
    
    count = [0] * range_size
    
    for num in arr:
        count[num + shift] += 1
    
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i - shift] * count[i])
    
    return sorted_arr

print("Примеры сортировки подсчетом:")

arr1 = [4, 2, 2, 8, 3, 3, 1]
print(f"\nИсходный массив: {arr1}")
print(f"Отсортированный массив: {counting_sort(arr1)}")

arr2 = [-3, -1, 4, 2, -2, 0, 1]
print(f"\nИсходный массив (с отрицательными): {arr2}")
print(f"Отсортированный массив: {counting_sort(arr2)}")