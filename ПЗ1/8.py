def closest(arr, x):
    left, right = 0, len(arr)-1

    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] == x:
            return arr[middle]
        elif arr[middle] >= x:
            left = middle
        else:
            right = middle
            
    candidates = []
    if left < len(arr):
        candidates.append(arr[left])
    if right > 0:
        candidates.append(arr[right])

    min_diff = min(abs(x - c) for c in candidates)
    return [c for c in candidates if abs(x - c) == min_diff]


A = [65, 43, 23, 11, 7]
B = [3, 54, 23, 9, 65]

for i in B:
    print(f'{i} - {closest(A, i)}')