#Задача № 8
#Дано число N (> 0) и непустая очередь. Создать функцию для извлечения из очереди N начальных элементов и отображения их значения (если очередь содержит менее N элементов, то извлечь все ее элементы). 

N = int(input("Введите число N: "))
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Очередь до извлечения элементов:", queue)

def extract_elements(N, queue):
    extracted_elements = []
    for _ in range(min(N, len(queue))):
        extracted_elements.append(queue.pop(0))
    return extracted_elements

extracted = extract_elements(N, queue)
print("Извлеченные элементы:", extracted)
print("Очередь после извлечения элементов:", queue)