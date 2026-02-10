import numpy as np
import random

L1 = [int(x) for x in np.random.randint(low=0, high=100, size=49)]
L1.insert(random.randint(1, len(L1)-1), 10)

print(f"L1: {L1}")

print("Первый элемент:", L1[0])
print("Сложность: O(1)")

print("Минимальное значение:", min(L1))
print("Сложность: O(n)")

print("Максимальное значение:", max(L1))
print("Сложность: O(n)")

print("Индекс элемента 10:", L1.index(10))
print("Сложность: O(n)")