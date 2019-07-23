class Node:
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class DoublyLinkedList:   
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
     
    # This node becomes the lesast recently used
    def reset(self, node):
        self.remove(node)
        self.pushFront(node)
        
    def remove(self, node):
        print(node.value)
        # prev = node.prev
        # next = node.next
        # prev.next = next
        # next.prev = prev
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def pushFront(self, node):
        currFront = self.head.next
        node.prev = self.head
        node.next = currFront
        currFront.prev = node
        self.head.next = node
        
    def removeBack(self):
        n = self.tail.prev
        prev = self.tail.prev.prev
        prev.next = self.tail
        self.tail.prev = prev
        return n

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = DoublyLinkedList()
        self.currSize = 0

    def get(self, key: int) -> int:
        print("get called")
        if key in self.cache:
            # if self.currSize > 1:
            self.queue.reset(self.cache[key]) #this is a node
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print("put called")
        if key in self.cache:
            # if self.currSize > 1:
            self.queue.reset(self.cache[key])
            self.cache[key].value = value
        else:
            self.cache[key] = Node(key, value)
            self.queue.pushFront(self.cache[key])
            self.currSize += 1
            
            if self.currSize > self.capacity:
                # Evict the tail node
                n = self.queue.removeBack()
                del self.cache[n.key]
                self.currSize -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)