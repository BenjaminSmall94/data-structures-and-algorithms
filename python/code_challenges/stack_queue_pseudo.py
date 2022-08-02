from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.queue = Stack()
        self.reversed_queue = Stack()

    def enqueue(self, value):
        self.queue.push(value)

    def dequeue(self):
        while not self.queue.is_empty():
            self.reversed_queue.push(self.queue.pop())
        returned_val = self.reversed_queue.pop()
        while not self.reversed_queue.is_empty():
            self.queue.push(self.reversed_queue.pop())
        return returned_val
