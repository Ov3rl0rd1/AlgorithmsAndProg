#Задача № 5*
#Реализуйте собственное множество на основе хеш-таблицы.
#Условия: 
#1. 	Элемент во множество добавляется по последней цифре числа. Например, если имеется число 3456, то оно будет добавлено на позицию с ключом 6.
#2. Ячеек во множестве 10 (ключи хеш-таблицы от 0 до 9).
#Реализуйте функции: 
#•	добавления элементов
#•	поиск и вывод всех элементов ячейки
#•	поиск конкретного числа в множестве
#•	удаление элемента из множества.

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

my_set = CustomSet()

print("Добавление элементов:")

elements = [3456, 123, 7890, 456, 789, 2021, 555, 111, 2, 98]
for elem in elements:
    my_set.add(elem)

# Вывод структуры хеш-таблицы
my_set.display()
print()

print("Поиск и вывод всех элементов ячейки:")
for cell_key in [0, 1, 6, 9]:
    elements_in_cell = my_set.get_cell_elements(cell_key)
    print(f"Элементы в ячейке {cell_key}: {elements_in_cell}")
print()

print("Поиск конкретного числа:")
search_numbers = [3456, 7890, 100, 555]
for num in search_numbers:
    found = my_set.search(num)
    if found:
        hash_key = num % 10
        print(f"Число {num} найдено в ячейке {hash_key}")
    else:
        print(f"Число {num} не найдено в множестве")
print()

print("Удаление элементов:")
remove_numbers = [3456, 789, 100, 111]
for num in remove_numbers:
    print(f"Попытка удалить {num}:")
    my_set.remove(num)

# после удаления
print()
my_set.display()
print()

print("Попытка добавить дубликат:")
my_set.add(123)
my_set.add(123)
print()

print(f"Финальное множество: {my_set}")
print()