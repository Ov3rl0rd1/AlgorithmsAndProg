#Задача № 4
#Дан набор из N чисел (N > 10). Создать очередь, содержащую данные числа в указанном порядке (первое число будет размещаться в начале очереди, последнее — в конце). Извлечь из очереди все элементы и вывести их значения. Вывести также количество извлеченных элементов N.
#Очередь необходимо реализовать, используя:
#c.	Встроенный список (list)
#d.	Класс collections.deque
#e.	Класс queue.Queue

#c

queue_list = []

N = int(input("Введите количество чисел: "))
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    queue_list.append(num)
    
print("Очередь (list):", queue_list)

count = 0
while queue_list:
    print(queue_list.pop(0))
    count += 1
    
print(f"Количество извлеченных элементов: {count}")

#d

from collections import deque

queue_deque = deque()
N = int(input("Введите количество чисел: "))
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    queue_deque.append(num)
    
print("Очередь (deque):", queue_deque)

count = 0
while queue_deque:
    print(queue_deque.popleft())
    count += 1
    
print(f"Количество извлеченных элементов: {count}")

#e

from queue import Queue

queue_queue = Queue()
N = int(input("Введите количество чисел: "))
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    queue_queue.put(num)
    
print("Очередь (Queue):", list(queue_queue.queue))

count = 0
while not queue_queue.empty():
    print(queue_queue.get())
    count += 1
    
print(f"Количество извлеченных элементов: {count}")
    