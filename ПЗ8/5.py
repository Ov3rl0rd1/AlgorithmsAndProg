#Задача № 5
#С помощью промежуточного этапа сортировки подсчетом решите задачу:
#Дано два числа X и Y без ведущих нулей. Необходимо проверить, можно ли получить одно число из другого перестановкой цифр.

def counting_sort_digits(digits):
    count = [0] * 10
    
    for digit in digits:
        count[digit] += 1
    
    sorted_digits = []
    for i in range(10):
        sorted_digits.extend([i] * count[i])
    
    return sorted_digits

def can_rearrange(x, y):
    digits_x = [int(d) for d in str(x)]
    digits_y = [int(d) for d in str(y)]
    
    if len(digits_x) != len(digits_y):
        return False
    
    sorted_x = counting_sort_digits(digits_x)
    sorted_y = counting_sort_digits(digits_y)
    
    return sorted_x == sorted_y

print("Проверка возможности получить одно число из другого перестановкой цифр:\n")

test_cases = [
    (123, 321),
    (123, 456),
    (1234, 4321),
    (1023, 3210),
    (100, 10)
]

for x, y in test_cases:
    result = can_rearrange(x, y)
    print(f"Числа {x} и {y}: {result}")
