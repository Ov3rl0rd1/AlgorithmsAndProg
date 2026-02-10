import numpy as np

L1 = [int(x) for x in np.random.randint(low=0, high=100, size=49)]
L1.append(10)
L1.sort()

print(f"L1: {L1}")

def search(arr:list[int], x:int) -> int:
    left, right = 0, len(arr)-1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < x:
            left = middle + 1
        else:
            right = middle
    return left

print(f"Индекс элемента 10: {search(L1, 10)}")
print("Сложность алгоритма: O(log n)")