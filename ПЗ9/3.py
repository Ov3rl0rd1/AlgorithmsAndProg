#Задача № 3
#Создайте 2 текстовых файла и заполните их разным текстом.
#С помощью множеств определите:
#1.	Уникальные слова в файле 1 (без дубликатов). Уникальные слова в файле 2.
#2.	Уникальные слова в двух файлах (если бы текст в двух файлах необходимо было объединить).
#3.	Уникальные слова, которые встречаются только в файле 1 и отсутствуют в файле 2.
#4.	Уникальные слова, которые встречаются лишь в одном файле из двух (то есть слова, которые находятся только в файле 1 и отсутствуют в файле 2, а также слова, которые находятся только в файле 2 и отсутствуют в файле 1).
#5.	Уникальные слова, которые встречаются одновременно в обоих файлах.
#6.	Создайте подмножество слов из множества всех слов в файле 1.
#Создайте подмножество слов из множества всех слов в файле 2.
#Определите, равны ли два подмножества.

import re

def get_words_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b[a-z]+\b', text)
            return set(words)
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return set()


file1_words = get_words_from_file('C:\\Users\\nrbud\\Desktop\\AlgorithmsAndProg\\ПЗ9\\file1.txt')
file2_words = get_words_from_file('C:\\Users\\nrbud\\Desktop\\AlgorithmsAndProg\\ПЗ9\\file2.txt')
    
print("1. Уникальные слова в файле 1:")
print(f"   Множество: {sorted(file1_words)}")
print(f"   Количество: {len(file1_words)} слов")
print()
    
print("1. Уникальные слова в файле 2:")
print(f"   Множество: {sorted(file2_words)}")
print(f"   Количество: {len(file2_words)} слов")
print()
    
all_words = file1_words.union(file2_words)
print("2. Уникальные слова в двух файлах (объединение):")
print(f"   Множество: {sorted(all_words)}")
print(f"   Количество: {len(all_words)} слов")
print()
    
only_file1 = file1_words.difference(file2_words)
print("3. Слова только в файле 1 (отсутствуют в файле 2):")
print(f"   Множество: {sorted(only_file1)}")
print(f"   Количество: {len(only_file1)} слов")
print()
    
# 4. Слова только в одном файле (симметрическая разница)
only_one_file = file1_words.symmetric_difference(file2_words)
print("4. Слова только в одном файле (в одном, но не в другом):")
print(f"   Множество: {sorted(only_one_file)}")
print(f"   Количество: {len(only_one_file)} слов")
print()
    
# 5. Общие слова в обоих файлах (пересечение)
common_words = file1_words.intersection(file2_words)
print("5. Общие слова в обоих файлах (пересечение):")
print(f"   Множество: {sorted(common_words)}")
print(f"   Количество: {len(common_words)} слов")
print()
    
# 6. Создание подмножеств и проверка равенства
print("6. Подмножества и проверка равенства:")
# Создаем подмножества (берем первые 3 элемента для примера)
subset1 = set(sorted(file1_words)[:3])
subset2 = set(sorted(file2_words)[:3])
    
print(f"   Подмножество 1 (из файла 1): {sorted(subset1)}")
print(f"   Подмножество 2 (из файла 2): {sorted(subset2)}")
print(f"   Равны ли подмножества: {subset1 == subset2}")
    
# Одинаковые подмножества
subset3 = set(sorted(file1_words)[:2])
subset4 = set(sorted(file2_words)[:2])
    
identical_subset1 = set(sorted(common_words)[:2]) if common_words else set()
identical_subset2 = identical_subset1.copy()
    
if identical_subset1:
    print(f"   Идентичное подмножество 1: {sorted(identical_subset1)}")
    print(f"   Идентичное подмножество 2: {sorted(identical_subset2)}")
    print(f"   Равны ли идентичные подмножества: {identical_subset1 == identical_subset2}")
print()