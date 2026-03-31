#Задача № 1
#Реализуйте однонаправленный связный список путем создания класса в Python. При этом в виде методов класса для однонаправленного связного списка реализовать операции:
#•	Чтение всех элементов.
#•	Вставка элемента в конец связного списка.
#•	Вставка элемента в начало связного списка.
#•	Удаление элемента с конца связного списка.
#•	Удаление элемента с начала связного списка.
#•	Поиск элемента в связном списке.
#•	Вставка элемента после указанного элемента.
#•	Удаление указанного элемента.

class Node:
    def __init__(self, data):
        self.data = data
        self.next:Node = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head:Node = None
        
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