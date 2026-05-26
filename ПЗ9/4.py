#Задача № 4
#Дана последовательность положительных чисел длинной N и число Х. Создайте множество из последовательности чисел.
#Необходимо найти два разных числа A и B из множества, таких что A + B = X или вернуть пару 0, 0, если такой пары нет.
#Пример:
#Последовательность чисел: 1, 10, 2, 4, 16, 7, 1, 2, 10, 7, 3.
#N = 11, X = 6.
#Множество чисел: 1, 10, 2, 4, 16, 7, 3.
#Вывод: 2, 4.

def find_pair_sum(sequence, target_sum):
    num_set = set(sequence)
    
    print(f"Последовательность: {sequence}")
    print(f"N = {len(sequence)}")
    print(f"X = {target_sum}")
    print(f"Множество чисел: {sorted(num_set)}")
    
    for num in num_set:
        needed = target_sum - num
        
        if needed != num and needed in num_set:
            return (min(num, needed), max(num, needed))
    
    return (0, 0)


def find_all_pairs_sum(sequence, target_sum):
    num_set = set(sequence)
    pairs = []
    used = set()
    
    for num in num_set:
        needed = target_sum - num
        
        if needed != num and needed in num_set:
            pair = (min(num, needed), max(num, needed))
            if pair not in used:
                pairs.append(pair)
                used.add(pair)
    
    return pairs

    
# Пример из задания
sequence1 = [1, 10, 2, 4, 16, 7, 1, 2, 10, 7, 3]
target1 = 6
result1 = find_pair_sum(sequence1, target1)
print(f"Результат: {result1}")
print()

# Есть решение
print("\nТест 2: Поиск пары с суммой 15")
sequence2 = [1, 5, 7, -2, 8, 10, 3]
target2 = 15
result2 = find_pair_sum(sequence2, target2)
print(f"Результат: {result2}")
print()

# Нет решения
print("Тест 3: Поиск пары с суммой 100")
sequence3 = [1, 2, 3, 4, 5]
target3 = 100
result3 = find_pair_sum(sequence3, target3)
print(f"Результат: {result3}")
print()

# Множество решений
print("Тест 4: Поиск ВСЕ пары с суммой 10")
sequence4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target4 = 10
print(f"Последовательность: {sequence4}")
print(f"X = {target4}")
print(f"Множество чисел: {sorted(set(sequence4))}")
all_pairs = find_all_pairs_sum(sequence4, target4)
print(f"Все пары: {all_pairs}")
print()

# С нулями и отрицательными числами
print("Тест 5: Поиск пары с суммой 0")
sequence5 = [-5, -3, 0, 3, 5, 8]
target5 = 0
result5 = find_pair_sum(sequence5, target5)
print(f"Результат: {result5}")
print()