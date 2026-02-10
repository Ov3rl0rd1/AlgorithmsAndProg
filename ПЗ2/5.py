# Сортировка пузырьком.
# Проходим по списку, сравнивая соседние элементы. Если они расположенны не в порядке возрастания, то меняем их местами. 
# Повторяем процесс для всех элементов.

list1 = [6, 12, 4, 3, 8]

# Только цикл for
def sort1(arr:list[int]) -> list[int]:
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Только цикл while
def sort2(arr:list[int]) -> list[int]:
    i = 0
    while i < len(arr)-1:
        j = 0
        while j < len(arr)-i-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1
    return arr

print(sort1(list1.copy()))
print(sort2(list1.copy()))