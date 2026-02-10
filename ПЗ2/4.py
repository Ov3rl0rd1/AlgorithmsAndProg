list1 = [6, 12, 4, 3, 8]

# Сортировка выбором.
# Выбираем наименьший элемент и меняем его местами с первым элементом, затем повторяем для оставшейся части списка.

# Только цикл for
def sort2(arr:list[int]) -> list[int]:
    for i in range(len(arr)):
        minInx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minInx]:
                minInx = j
        arr[i], arr[minInx] = arr[minInx], arr[i]
    return arr

# Только цикл while
def sort3(arr:list[int]) -> list[int]:
    i = 0
    while i < len(arr):
        minInx = i
        j = i+1
        while j < len(arr):
            if arr[j] < arr[minInx]:
                minInx = j
            j += 1
        arr[i], arr[minInx] = arr[minInx], arr[i]
        i += 1
    return arr

# Через 2 массива
def sort4(arr:list[int]) -> list[int]:
    sortedArr = []
    while arr:
        minInx = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[minInx]:
                minInx = i
        sortedArr.append(arr.pop(minInx))
    return sortedArr

# Через 1 массив
def sort5(arr:list[int]) -> list[int]:
    return sort2(arr)

print(sort2(list1.copy()))
print(sort3(list1.copy()))
print(sort4(list1.copy()))
print(sort5(list1.copy()))