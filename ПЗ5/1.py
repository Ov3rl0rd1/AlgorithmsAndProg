#Задачи
#При выполнении задач не допускается обращение к произвольному элементу стека или очереди, необходимо учитывать особенности указанных структур данных [].
#Задача № 1
#Дано число N (> 0) и набор из N чисел. Создать стек, содержащий исходные числа (последнее число будет вершиной стека). Извлечь из стека все элементы и вывести их значения. Вывести также количество извлеченных элементов N.
#Стек необходимо реализовать, используя:
#a.	Встроенный список (list)
#b.	Класс collections.deque
#c.	Класс queue.LifoQueue

from collections import deque
from queue import LifoQueue

N = int(input("Введите количество чисел: "))
numbers = []

# a

stack_list = []
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    stack_list.append(num)
    
print("Стек (list):", stack_list)

count = 0
while stack_list:
    print(stack_list.pop())
    count += 1
    
print(f"Количество извлеченных элементов: {count}")

# b

stack_deque = deque()
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    stack_deque.append(num)
    
print("Стек (deque):", stack_deque)
count = 0
while stack_deque:
    print(stack_deque.pop())
    count += 1
    
print(f"Количество извлеченных элементов: {count}")

# c

stack_lifo = LifoQueue()
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    stack_lifo.put(num)
    
print("Стек (LifoQueue):", list(stack_lifo.queue))
count = 0
while not stack_lifo.empty():
    print(stack_lifo.get())
    count += 1

print(f"Количество извлеченных элементов: {count}")