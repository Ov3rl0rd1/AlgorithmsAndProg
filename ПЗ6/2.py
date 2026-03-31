#Задача № 2
#Реализуйте двунаправленный связный список путем создания класса в Python. При этом в виде методов класса для двунаправленного связного списка реализуйте операции:
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
        self.prev:Node = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def delete_from_end(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
        
    def delete_from_beginning(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None
        
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
        while current_node:
            if current_node.data == prev_data:
                new_node.next = current_node.next
                new_node.prev = current_node
                if current_node.next:
                    current_node.next.prev = new_node
                else:
                    self.tail = new_node
                current_node.next = new_node
                return
            current_node = current_node.next
            
    def delete_node(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                return
            current_node = current_node.next
            
    def read_all(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements