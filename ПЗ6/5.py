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

class Queue:
    def __init__(self):
        self.linked_list = SinglyLinkedList()
    
    def enqueue(self, data):
        self.linked_list.insert_at_end(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        first_element = self.linked_list.head.data
        self.linked_list.delete_from_beginning()
        return first_element
    
    def is_empty(self):
        return self.linked_list.head is None
    
    def size(self):
        return len(self.linked_list)

import time

class SingleProcessorSystem:
    def __init__(self):
        self.queue = Queue()
        self.processed_count = 0
    
    def add_request(self, request_id):
        self.queue.enqueue(request_id)
        print(f"Заявка {request_id} добавлена в очередь")
    
    def process_all_requests(self):
        print(f"\nНачало обработки заявок\n")
        
        while not self.queue.is_empty():
            request_id = self.queue.dequeue()
            print(f"Обработка заявки {request_id}...")
            self.processed_count += 1
            print(f"+ Заявка {request_id} обработана")


system = SingleProcessorSystem()

print("\nДобавление заявок в очередь:")
for i in range(1, 11):
    system.add_request(i)

print(f"\nВсего заявок в очереди: {system.queue.size()}")

system.process_all_requests()

print("\n\n")
print(f"Обработано заявок: {system.processed_count}")

