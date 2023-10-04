# Implement a queue using the stack data structure

class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return None
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def is_empty(self):
        return not self.stack_enqueue and not self.stack_dequeue

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

queue = QueueUsingStack()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

queue.enqueue(4)

print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4
print(queue.dequeue())  # Output: None (queue is empty)

