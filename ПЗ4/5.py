#Реализовать быструю сортировку и сортировку слиянием на Python через создание двух соответствующих функций. Предусмотреть следующие возможности:
#a.	визуализация (через консоль) всех шагов алгоритма, включая массив и (или) подмассивы, с которыми работает алгоритм на текущем шаге;
#b.	для быстрой сортировки – выбор опорного элемента (первый, последний, случайный);
#c.	выбор типа сортировки (по возрастанию, по убыванию);
#Проверить созданные функции на следующих массивах:
#•	массив из исходных данных;
#•	массив 10 случайных целых чисел (без повторов) в диапазоне [0; 100];
#•	массив 20 случайных целых чисел (с повторами) в диапазоне [0; 100];
#•	массив 30 случайных целых чисел (с повторами) в диапазоне [-100; 100];
#•	массив 50 случайных целых чисел (с повторами) в диапазоне [-1000; 1000].
# Массивы из случайных чисел генерировать при помощи numpy

import numpy as np
import random
from typing import List, Any

maxDepth = 0

def _print_step(prefix: str, depth: int, lst: List[Any]):
    global maxDepth
    indent = '  ' * depth
    maxDepth = max(depth, maxDepth)
    print(f"{indent}{prefix}: {lst}")


def quick_sort(arr: List[int], *, pivot_type: str = 'middle', ascending: bool = True, visualize: bool = True, depth: int = 0) -> List[int]:
	if visualize:
		_print_step('call quick_sort', depth, arr)

	if len(arr) <= 1:
		if visualize:
			_print_step('return quick_sort', depth, arr[:])
		return arr[:]

	if pivot_type == 'first':
		pivot = arr[0]
	elif pivot_type == 'last':
		pivot = arr[-1]
	elif pivot_type == 'random':
		pivot = int(random.choice(arr))
	else:
		pivot = arr[len(arr) // 2]

	left = []
	middle = []
	right = []

	for x in arr:
		if (x < pivot and ascending) or (x > pivot and not ascending):
			left.append(x)
		elif (x > pivot and ascending) or (x < pivot and not ascending):
			right.append(x)
		else:
			middle.append(x)

	sorted_left = quick_sort(left, pivot_type=pivot_type, ascending=ascending, visualize=visualize, depth=depth + 1)
	sorted_right = quick_sort(right, pivot_type=pivot_type, ascending=ascending, visualize=visualize, depth=depth + 1)

	result = sorted_left + middle + sorted_right

	if visualize:
		_print_step('return quick_sort', depth, result)
	return result


def merge_sort(arr: List[int], *, ascending: bool = True, visualize: bool = True, depth: int = 0) -> List[int]:
	if visualize:
		_print_step('call merge_sort', depth, arr)

	if len(arr) <= 1:
		if visualize:
			_print_step('return merge_sort', depth, arr[:])
		return arr[:]

	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]

	sorted_left = merge_sort(left, ascending=ascending, visualize=visualize, depth=depth + 1)
	sorted_right = merge_sort(right, ascending=ascending, visualize=visualize, depth=depth + 1)

	i = j = 0
	merged: List[int] = []
	while i < len(sorted_left) and j < len(sorted_right):
		if ascending:
			if sorted_left[i] <= sorted_right[j]:
				merged.append(sorted_left[i])
				i += 1
			else:
				merged.append(sorted_right[j])
				j += 1
		else:
			if sorted_left[i] >= sorted_right[j]:
				merged.append(sorted_left[i])
				i += 1
			else:
				merged.append(sorted_right[j])
				j += 1
	merged.extend(sorted_left[i:])
	merged.extend(sorted_right[j:])

	if visualize:
		_print_step('return merge_sort', depth, merged)
	return merged

np.random.seed(0)
random.seed(0)

original = [38, 27, 43, 3, 9, 82]
a10 = [int(x) for x in list(np.random.choice(np.arange(0, 101), size=10, replace=False))]
a20 = [int(x) for x in list(np.random.randint(0, 101, size=20))]
a30 = [int(x) for x in list(np.random.randint(-100, 101, size=30))]
a50 = [int(x) for x in list(np.random.randint(-1000, 1001, size=50))]

arrays = [('original', original),
			('10_unique_0_100', a10),
			('20_repeat_0_100', a20),
			('30_repeat_-100_100', a30),
			('50_repeat_-1000_1000', a50)]

with open('sorting_results.txt', 'w') as f:
    f.write('=== Sorting Algorithm Results ===\n\n')
    for name, arr in arrays:
        f.write(f'=== Test: {name} size={len(arr)} ===\n')
        f.write(f'Input: {arr}\n\n')
        f.write('-- Quick Sort (pivot=first, ascending) --\n')
        qs1 = quick_sort(arr, pivot_type='first', ascending=True, visualize=True)
        f.write(f"Rec Depth {maxDepth}\n")
        f.write(f'Result quick_sort (first, asc): {qs1}\n\n')
        f.write('-- Quick Sort (pivot=random, descending) --\n')
        maxDepth = 0
        qs_rand = quick_sort(arr, pivot_type='random', ascending=False, visualize=True)
        f.write(f"Rec Depth {maxDepth}\n")
        f.write(f'Result quick_sort (random, asc): {qs_rand}\n\n')
        f.write('-- Merge Sort (ascending) --\n')
        ms = merge_sort(arr, ascending=True, visualize=False)
        f.write(f'Result merge_sort (asc): {ms}\n\n')
        f.write('-- Merge Sort (descending) --\n')
        ms_desc = merge_sort(arr, ascending=False, visualize=False)
        f.write(f'Result merge_sort (desc): {ms_desc}\n\n')