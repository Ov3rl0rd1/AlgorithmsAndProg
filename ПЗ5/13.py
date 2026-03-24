#Задача № 13
#Даны две непустые очереди. Элементы каждой из очередей упорядочены по возрастанию (в направлении от начала очереди к концу). Объединить очереди в одну с сохранением упорядоченности элементов. 
#Очередь необходимо реализовать, используя:
#c.	Класс collections.deque
#d.	Класс queue.Queue

#c

from collections import deque

def merge_queues(queue1, queue2):
    result_queue = deque()
    
    while queue1 and queue2:
        if queue1[0] < queue2[0]:
            result_queue.append(queue1.popleft())
        else:
            result_queue.append(queue2.popleft())
    
    result_queue.extend(queue1)
    result_queue.extend(queue2)
    
    return result_queue

queue1 = deque([1, 3, 5])
queue2 = deque([2, 4, 6])

print("Очередь 1:", queue1)
print("Очередь 2:", queue2)

result_queue = merge_queues(queue1, queue2)

print("Результат объединения:", result_queue)

#d

from queue import Queue

def merge_queues(queue1, queue2):
    result_queue = Queue()
    
    while not queue1.empty() and not queue2.empty():
        if queue1.queue[0] < queue2.queue[0]:
            result_queue.put(queue1.get())
        else:
            result_queue.put(queue2.get())
    
    while not queue1.empty():
        result_queue.put(queue1.get())
        
    while not queue2.empty():
        result_queue.put(queue2.get())
    
    return result_queue

queue1 = Queue()
for num in [1, 3, 5]:
    queue1.put(num)

queue2 = Queue()
for num in [2, 4, 6]:
    queue2.put(num)
    

print("Очередь 1:", list(queue1.queue))
print("Очередь 2:", list(queue2.queue))

result_queue = merge_queues(queue1, queue2)
print("Результат объединения:", list(result_queue.queue))