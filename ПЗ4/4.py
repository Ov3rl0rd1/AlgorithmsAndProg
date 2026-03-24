arr = [38, 27, 43, 3, 9, 82]

def print_step(prefix, depth, lst):
    indent = '  ' * depth
    print(f"{depth}.{indent}{prefix}: {lst}")


def quick_sort(a, depth=0):
    print_step('call quick_sort', depth, a)
    if len(a) <= 1:
        print_step('return quick_sort', depth, a)
        return a[:]

    pivot = a[len(a) // 2]
    left = []
    middle = []
    right = []

    for x in a:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    sorted_left = quick_sort(left, depth + 1)
    sorted_right = quick_sort(right, depth + 1)

    result = sorted_left + middle + sorted_right
    print_step('return quick_sort', depth, result)
    return result


def merge_sort(a, depth=0):
    print_step('call merge_sort', depth, a)
    if len(a) <= 1:
        print_step('return merge_sort', depth, a)
        return a[:]

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    sorted_left = merge_sort(left, depth + 1)
    sorted_right = merge_sort(right, depth + 1)

    i = j = 0
    merged = []
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1
    merged.extend(sorted_left[i:])
    merged.extend(sorted_right[j:])

    print_step('return merge_sort', depth, merged)
    return merged


print('Исходный массив:', arr)
print('\nБыстрая сортировка')

qs = quick_sort(arr)
print('Результат быстрой сортировки:', qs)

print('\nСортировки слиянием')
ms = merge_sort(arr)
print('Результат сортировки слиянием:', ms)