#Задача № 2
#Имеется ряд словарей с пересекающимися ключами (значения – положительные числа). Напишите 2 функции, которые производят с массивом словарей следующие операции:
#•	функция max_dct(*dicts) формирует новый словарь по правилу:
#o	если в исходных словарях имеются повторяющиеся ключи, среди их значений выбирается максимальное и присваивается этому ключу (например, в словаре_1 есть ключ "a" со значением 5, и в словаре_2 есть ключ "a", но со значением 9. Выбирается максимальное значение, т.е. 9, и присваивается ключу "a" в уже новом словаре).  
#o	если ключ не повторяется, то он просто переносится со своим значением в новый словарь (например, ключ "c" встретился только у одного словаря, а у других его нет. Следовательно, переносим в новый словарь этот ключ вместе с его значением). Сформированный словарь возвращаем.
#•	функция sum_dct(*dicts) суммирует значения повторяющихся ключей. Значения остальных ключей остаются исходными. (Проводятся операции по аналогу первой функции, но берутся не максимумы, а суммы значений одноименных ключей). Функция возвращает сформированный словарь.

def max_dct(*dicts):
    result = {}
    
    for dict_item in dicts:
        for key, value in dict_item.items():
            if key in result:
                result[key] = max(result[key], value)
            else:
                result[key] = value
    
    return result


def sum_dct(*dicts):
    result = {}
    
    for dict_item in dicts:
        for key, value in dict_item.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    
    return result


dict1 = {"a": 5, "b": 10, "c": 3}
dict2 = {"a": 9, "b": 2, "d": 7}
dict3 = {"a": 3, "e": 15, "c": 8}
    
print("Исходные словари:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict3 = {dict3}")
print()
    
result_max = max_dct(dict1, dict2, dict3)
print("Результат max_dct(dict1, dict2, dict3):")
print(result_max)
print("Объяснение:")
print("  'a': max(5, 9, 3) = 9")
print("  'b': max(10, 2) = 10")
print("  'c': max(3, 8) = 8")
print("  'd': 7 (только в dict2)")
print("  'e': 15 (только в dict3)")
print()
    
result_sum = sum_dct(dict1, dict2, dict3)
print("Результат sum_dct(dict1, dict2, dict3):")
print(result_sum)
print("Объяснение:")
print("  'a': 5 + 9 + 3 = 17")
print("  'b': 10 + 2 = 12")
print("  'c': 3 + 8 = 11")
print("  'd': 7 (только в dict2)")
print("  'e': 15 (только в dict3)")
print()