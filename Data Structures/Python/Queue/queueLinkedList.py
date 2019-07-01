class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        if self.front == None:
            return True
        return False

    def enqueue(self, val):
        if self.front == None:
            self.front = Node(val)
            self.back = self.front
        else:
            temp = self.back
            self.back = Node(val)
            temp.next = self.back

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        else:
            temp = self.front
            self.front = temp.next
            temp = None
            if self.front == None:
                self.back = None

    def printQueue(self):
        if self.isEmpty():
            print("None")
            print("front: " + str(self.front))
            print("back: " + str(self.back))
            print()
            return
        else:
            temp = self.front
            while temp is not None:
                print(str(temp.val) + "->", end =" ")
                temp = temp.next
            print("None")
            print("front: " + str(self.front.val))
            print("back: " + str(self.back.val))
            print()

q = Queue() 
q.printQueue()
q.enqueue(10) 
q.printQueue()
q.enqueue(20) 
q.printQueue()
q.dequeue() 
q.printQueue()
q.dequeue() 
q.printQueue()
q.enqueue(30) 
q.printQueue()
q.enqueue(40) 
q.printQueue()
q.enqueue(50) 
q.printQueue()
