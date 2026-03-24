#Задача № 9
#Дана непустая очередь. Извлекать из очереди элементы, пока значение начального элемента очереди не станет четным, и выводить значения извлеченных элементов (если очередь не содержит элементов с четными значениями, то извлечь все ее элементы).

queue = [1, 3, 5, 7, 8, 10]

print("Очередь до извлечения элементов:", queue)

def extract_until_even(queue):
    extracted_elements = []
    while queue and queue[0] % 2 != 0:
        extracted_elements.append(queue.pop(0))
    return extracted_elements

extracted = extract_until_even(queue)
print("Извлеченные элементы:", extracted)
print("Очередь после извлечения элементов:", queue)