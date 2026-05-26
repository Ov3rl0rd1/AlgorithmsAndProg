#Задача № 6*
#Решите Задачу № 4, используя собственное множество из задачи № 5.

class CustomSet:
    def __init__(self):
        self.hash_table = {i: [] for i in range(10)}
        self.size = 0
    
    def _get_hash(self, num):
        return abs(num) % 10
    
    def add(self, element):
        hash_key = self._get_hash(element)
        
        if element not in self.hash_table[hash_key]:
            self.hash_table[hash_key].append(element)
            self.size += 1
            print(f"Элемент {element} добавлен в ячейку {hash_key}")
        else:
            print(f"Элемент {element} уже существует в множестве")
    
    def get_cell_elements(self, cell_key):
        if 0 <= cell_key <= 9:
            return self.hash_table[cell_key]
        else:
            print(f"Ошибка: ключ {cell_key} должен быть от 0 до 9")
            return []
    
    def search(self, element):
        hash_key = self._get_hash(element)
        return element in self.hash_table[hash_key]
    
    def remove(self, element):
        hash_key = self._get_hash(element)
        
        if element in self.hash_table[hash_key]:
            self.hash_table[hash_key].remove(element)
            self.size -= 1
            print(f"Элемент {element} удален из множества")
        else:
            print(f"Элемент {element} не найден в множестве")
    
    def display(self):
        print("\nСодержимое хеш-таблицы:")
        
        for key in range(10):
            print(f"Ячейка {key}: {self.hash_table[key]}")
        print(f"Всего элементов: {self.size}")
    
    def __str__(self):
        all_elements = []
        for key in range(10):
            all_elements.extend(self.hash_table[key])
        return f"CustomSet({sorted(all_elements)})"
    
    def get_all_elements(self) -> list:
        all_elements = []
        for key in range(10):
            all_elements.extend(self.hash_table[key])
            
        return all_elements
        


def find_pair_sum_custom_set(sequence, target_sum):
    custom_set = CustomSet()
    
    print(f"Исходная последовательность: {sequence}")
    print(f"N = {len(sequence)}")
    print(f"X = {target_sum}")
    
    for num in sequence:
        custom_set.add(num)
    
    all_elements = custom_set.get_all_elements()
    print(f"Множество (уникальные элементы): {sorted(set(all_elements))}")
    print()
    
    custom_set.display()
    print()
    
    for num in set(all_elements):
        needed = target_sum - num
        
        if needed != num and custom_set.search(needed):
            return (min(num, needed), max(num, needed))
    
    return (0, 0)


def find_all_pairs_custom_set(sequence, target_sum):
    custom_set = CustomSet()
    
    for num in sequence:
        custom_set.add(num)
    
    all_elements = set(custom_set.get_all_elements())
    pairs = []
    used = set()
    
    for num in all_elements:
        needed = target_sum - num
        
        if needed != num and custom_set.search(needed):
            pair = (min(num, needed), max(num, needed))
            if pair not in used:
                pairs.append(pair)
                used.add(pair)
    
    return pairs
    
# Пример из задания
sequence1 = [1, 10, 2, 4, 16, 7, 1, 2, 10, 7, 3]
target1 = 6
result1 = find_pair_sum_custom_set(sequence1, target1)
print(f"Результат: {result1}")
print()

print("Тест: Нет решения")
sequence3 = [1, 2, 3, 4, 5]
target3 = 100
result3 = find_pair_sum_custom_set(sequence3, target3)
print(f"Результат: {result3}")
print()