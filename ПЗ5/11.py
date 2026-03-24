#Задача № 11
#Дано число N (> 0) и две непустые очереди. Создать функцию для перемещения N начальных элементов первой очереди в конец второй очереди. Если первая очередь содержит менее N элементов, то переместить из первой очереди во вторую все элементы.
#Очередь необходимо реализовать, используя:
#a.	Класс collections.deque
#b.	Класс queue.Queue

#a

from collections import deque

def move_elements(queue1, queue2, N):
    for _ in range(min(N, len(queue1))):
        queue2.append(queue1.popleft())
        
queue1 = deque([1, 2, 3, 4, 5])
queue2 = deque([6, 7, 8, 9, 10])

print("Очередь 1 до перемещения элементов:", queue1)
print("Очередь 2 до перемещения элементов:", queue2)

N = int(input("Введите число N: "))
move_elements(queue1, queue2, N)

print("Очередь 1 после перемещения элементов:", queue1)
print("Очередь 2 после перемещения элементов:", queue2)

#b

from queue import Queue

def move_elements(queue1, queue2, N):
    for _ in range(min(N, queue1.qsize())):
        queue2.put(queue1.get())
        
queue1 = Queue()
for i in range(1, 6):
    queue1.put(i)
    
queue2 = Queue()
for i in range(6, 11):
    queue2.put(i)
    
print("Очередь 1 до перемещения элементов:", list(queue1.queue))
print("Очередь 2 до перемещения элементов:", list(queue2.queue))

N = int(input("Введите число N: "))
move_elements(queue1, queue2, N)

print("Очередь 1 после перемещения элементов:", list(queue1.queue))
print("Очередь 2 после перемещения элементов:", list(queue2.queue))