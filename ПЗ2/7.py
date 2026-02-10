list1 = [6, 12, 4, 3, 8]

def simpleSort(arr:list[int], descending:bool=False, verbose:bool=False) -> list[int]:
    if verbose:
        print("Исходный массив:", arr)
        
    step = 0
        
    for i in range(len(arr)):
        minInx = i
        for j in range(i+1, len(arr)):
            step += 1
            if descending:
                if arr[j] > arr[minInx]:
                    minInx = j
            else:
                if arr[j] < arr[minInx]:
                    minInx = j
        arr[i], arr[minInx] = arr[minInx], arr[i]
        if verbose:
            print(f"{arr[i]} <-> {arr[minInx]}: {arr}")
    if verbose:
        print(f"Количество шагов: {step}")
    return arr

def bubbleSort(arr:list[int], descending:bool=False, verbose:bool=False) -> list[int]:
    if verbose:
        print("Исходный массив:", arr)
    step = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            step += 1
            if descending:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    if verbose:
                        print(f"{arr[j]} <-> {arr[j+1]}: {arr}")
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    if verbose:
                        print(f"{arr[j]} <-> {arr[j+1]}: {arr}")
    if verbose:
        print(f"Количество шагов: {step}")
    return arr

print(simpleSort(list1.copy(), descending=True, verbose=True))
print(bubbleSort(list1.copy(), descending=True, verbose=True))