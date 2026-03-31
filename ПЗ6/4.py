#Задача № 4
#На основе собственного класса реализуйте очередь через связный список. Используя такую очередь решите следующие задачи:
#a.	Дан набор из N чисел (N > 10). Создайте очередь, содержащую данные числа в указанном порядке (первое число будет размещаться в начале очереди, последнее – в конце). Извлеките из очереди все элементы и выведите их значения. Выведите также количество извлеченных элементов N.
#b.	Даны две очереди. Переместите все элементы первой очереди (в порядке от начала к концу) в конец второй очереди.
#c.	Дано число N (> 0) и две непустые очереди. Создайте функцию для перемещения N начальных элементов первой очереди в конец второй очереди. Если первая очередь содержит менее N элементов, то переместите из первой очереди во вторую все элементы.

#a

class Node:
    def __init__(self, data):
        self.data = data
        self.next:Node = None
        self.prev:Node = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head:Node = None
        
    def __len__(self):
        return len(self.read_all())
    
    def __str__(self):
        return str(self.read_all())
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last_node = self.head
        while second_last_node.next and second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None
        
    def delete_from_beginning(self):
        if not self.head:
            return
        self.head = self.head.next
        
    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False
    
    def insert_after(self, prev_data, data):
        new_node = Node(data)
        current_node = self.head
        while current_node and current_node.data != prev_data:
            current_node = current_node.next
        if not current_node:
            raise ValueError()
        new_node.next = current_node.next
        current_node.next = new_node
        
    def delete_element(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != key:
            current_node = current_node.next
        if not current_node.next:
            raise KeyError()
        current_node.next = current_node.next.next
        
    def read_all(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements
    
#a
    
queueA = SinglyLinkedList()
    
N = int(input("Введите количество чисел: "))
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    queueA.insert_at_end(num)
    
print("Очередь (SinglyLinkedList):", queueA.read_all())

#b

queueA = SinglyLinkedList()
queueB = SinglyLinkedList()

for i in range(1, 11):
    queueA.insert_at_beginning(11-i)
    queueB.insert_at_beginning(i)

print("1 лист до перестановки:", queueA)
print("2 лист до перестановки:", queueB)
    
for e in queueA.read_all():
    queueA.delete_from_beginning()
    queueB.insert_at_end(e)
    
print("1 лист после перестановки:", queueA)
print("2 лист после перестановки:", queueB)

#c

import random

def move_elements(queue1:SinglyLinkedList, queue2:SinglyLinkedList, N:int):
    for _ in range(min(N, len(queue1))):
        queue2.insert_at_end(queue1.head.data)
        queue1.delete_from_beginning()

queueA = SinglyLinkedList()
queueB = SinglyLinkedList()
    
N = int(input("Введите количество чисел: "))
for i in range(1, 11):
    queueA.insert_at_beginning(random.randint(1, 100))
    queueB.insert_at_beginning(random.randint(1, 100))
    
print("1 лист до перестановки:", queueA)
print("2 лист до перестановки:", queueB)

move_elements(queueA, queueB, N)

print("1 лист после перестановки:", queueA)
print("2 лист после перестановки:", queueB)