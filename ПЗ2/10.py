import numpy as np
import random

L1 = [int(x) for x in np.random.randint(low=0, high=100, size=49)]
L1.insert(random.randint(1, len(L1)-1), 10)

print(f"L1: {L1}")

print(f"Индекс элемента 10: {L1.index(10)}")
print("Сложность алгоритма: O(n)")