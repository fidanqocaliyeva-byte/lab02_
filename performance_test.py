import time

# 1. Linked List Performance (Playlist)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListTest:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

# 2. Stack Performance (Browser History)
class StackTest:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

# 3. Queue Performance (Print Service)
class QueueTest:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

# Testlərin icra olunması
sizes = [100, 1000, 10000]

print("--- PERFORMANS TEST NƏTİCƏLƏRİ ---")
for n in sizes:
    print(f"\nElement sayı: {n}")
    
    # Linked List Test
    start = time.time()
    ll = LinkedListTest()
    for i in range(n):
        ll.append(i)
    end = time.time()
    print(f"  Linked List (Playlist): {(end - start) * 1000:.4f} ms")
    
    # Stack Test
    start = time.time()
    st = StackTest()
    for i in range(n):
        st.push(i)
    end = time.time()
    print(f"  Stack (Browser History): {(end - start) * 1000:.4f} ms")
    
    # Queue Test
    start = time.time()
    q = QueueTest()
    for i in range(n):
        q.enqueue(i)
    end = time.time()
    print(f"  Queue (Print Service):   {(end - start) * 1000:.4f} ms")