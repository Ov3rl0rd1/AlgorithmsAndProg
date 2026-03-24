#Задача № 3
#Дан один непустой стек. Создать два новых стека, переместив в первый из них все элементы исходного стека с четными значениями, а во второй – с нечетными (элементы в новых стеках будут располагаться в порядке, обратном исходному; один из этих стеков может оказаться пустым).
#Стек необходимо реализовать, используя:
#a.	Класс collections.deque
#b.	Класс queue.LifoQueue

#a

from collections import deque

stack = deque()

N = int(input("Введите количество чисел: "))
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    stack.append(num)
    
print("Стек (deque):", stack)
    
stack_even = deque()
stack_odd = deque()

while stack:
    num = stack.pop()
    if num % 2 == 0:
        stack_even.append(num)
    else:
        stack_odd.append(num)
        
print("Стек с четными числами:", stack_even)
print("Стек с нечетными числами:", stack_odd)
        
#b
from queue import LifoQueue

stack = LifoQueue()

N = int(input("Введите количество чисел: "))
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    stack.put(num)
    
print("Стек (LifoQueue):", list(stack.queue))
    
stack_even = LifoQueue()
stack_odd = LifoQueue()

while not stack.empty():
    num = stack.get()
    if num % 2 == 0:
        stack_even.put(num)
    else:
        stack_odd.put(num)
        
print("Стек с четными числами:", list(stack_even.queue))
print("Стек с нечетными числами:", list(stack_odd.queue))