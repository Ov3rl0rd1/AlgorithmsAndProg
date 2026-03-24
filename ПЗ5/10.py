#Задача № 10
#Даны две очереди. Переместить все элементы первой очереди (в порядке от начала к концу) в конец второй очереди.

from collections import deque

queue1 = deque()
queue2 = deque()

for i in range(1, 6):
    queue1.append(i)
    
for i in range(6, 11):
    queue2.append(i)

print("Очередь 1 до перемещения элементов:", queue1)
print("Очередь 2 до перемещения элементов:", queue2)

while queue1:
    element = queue1.popleft()
    queue2.append(element)
    
print("Очередь 1 после перемещения элементов:", queue1)
print("Очередь 2 после перемещения элементов:", queue2)