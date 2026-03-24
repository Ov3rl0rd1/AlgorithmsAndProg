#Задача № 12
#Даны две непустые очереди. Очереди содержат одинаковое количество элементов. Объединить очереди в одну, в которой элементы исходных очередей чередуются (начиная с первого элемента первой очереди).
#

queue1 = [1, 3, 5]
queue2 = [2, 4, 6]

print("Очередь 1:", queue1)
print("Очередь 2:", queue2)

result_queue = []

while queue1 and queue2:
    result_queue.append(queue1.pop(0))
    result_queue.append(queue2.pop(0))
    
print("Результат объединения:", result_queue)