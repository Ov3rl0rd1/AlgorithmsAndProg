#Задача № 3
#Дана строка в виде случайной последовательности чисел от 0 до 9. 
#Требуется создать словарь, который в качестве ключей будет принимать данные числа (т.е. ключи будут иметь тип int), а в качестве значений – количество этих чисел в имеющейся последовательности. 
#Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

def count_it(sequence):
    digit_count = {}
    for digit in sequence:
        num = int(digit)
        digit_count[num] = digit_count.get(num, 0) + 1
    
    sorted_digits = sorted(digit_count.items(), key=lambda x: x[1], reverse=True)
    
    return {digit: count for digit, count in sorted_digits[:3]}

sequence1 = "1234567891234567891234567"
print("Последовательность:", sequence1)
print("3 самых часто встречаемых числа:", count_it(sequence1))

sequence2 = "000011112222332146132134329334444555566667777"
print("\nПоследовательность:", sequence2)
print("3 самых часто встречаемых числа:", count_it(sequence2))
