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
import threading

class RequestProcessor(threading.Thread):
    def __init__(self, processor_id, queue, process_time, results_list, lock):
        super().__init__()
        self.processor_id = processor_id
        self.queue = queue
        self.process_time = process_time
        self.results_list = results_list
        self.lock = lock
        self.daemon = True
        self.requests_processed = 0
    
    def run(self):
        while True:
            with self.lock:
                if self.queue.is_empty():
                    break
                request_id = self.queue.dequeue()
            
            start = time.time()
            print(f"[Обработчик {self.processor_id}] Обработка заявки {request_id}...")
            time.sleep(self.process_time)
            elapsed = time.time() - start
            
            self.requests_processed += 1
            
            with self.lock:
                self.results_list.append({
                    'processor_id': self.processor_id,
                    'request_id': request_id,
                    'process_time': elapsed
                })
            
            print(f"[Обработчик {self.processor_id}] + Заявка {request_id} обработана за {elapsed:.3f}с")


class MultiProcessorSystem:
    def __init__(self):
        self.queue = Queue()
        self.results_list = []
        self.lock = threading.Lock()
        self.processors = []
    
    def add_request(self, request_id):
        self.queue.enqueue(request_id)
    
    def process_with_processors(self, num_processors=3, processor_times=None):
        if processor_times is None:
            processor_times = [1.0, 1.01, 2.0]
        
        self.processors = []
        
        for i in range(num_processors):
            processor = RequestProcessor(
                processor_id=i+1,
                queue=self.queue,
                process_time=processor_times[i],
                results_list=self.results_list,
                lock=self.lock
            )
            self.processors.append(processor)
        
        start_time = time.time()
        
        for processor in self.processors:
            processor.start()
        
        for processor in self.processors:
            processor.join()
        
        total_time = time.time() - start_time
        return total_time


system = MultiProcessorSystem()

print("\nДобавление 20 заявок в очередь:")
for i in range(1, 21):
    system.add_request(i)
    if i % 5 == 0:
        print(f"    добавлено {i} заявок")

print(f"\nВсего заявок в очереди: {system.queue.size()}")
print(f"\nПараметры обработчиков:")
print(f"    Обработчик 1: 1.00 сек/заявка")
print(f"    Обработчик 2: 1.01 сек/заявка")
print(f"    Обработчик 3: 2.00 сек/заявка")

print(f"\nНачало обработки заявок 3 обработчиками\n")
total_time = system.process_with_processors(
    num_processors=3,
    processor_times=[1.0, 1.01, 2.0]
)

processor_stats = {}
for result in system.results_list:
    processor_id = result['processor_id']
    if processor_id not in processor_stats:
        processor_stats[processor_id] = {'count': 0, 'time': 0}
    processor_stats[processor_id]['count'] += 1
    processor_stats[processor_id]['time'] += result['process_time']

print("\n\n")
print(f"Общее время обработки всех 20 заявок: {total_time:.2f} сек")
print(f"\nСтатистика по обработчикам:")
for proc_id in sorted(processor_stats.keys()):
    stats = processor_stats[proc_id]
    print(f"    Обработчик {proc_id}: обработано {stats['count']} заявок, "
          f"общее время {stats['time']:.2f} сек")

print(f"\nВсего обработано заявок: {len(system.results_list)}")

 