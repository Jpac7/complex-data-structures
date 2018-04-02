# FIFO structure : FIRST IN FIRST OUT


class Queue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    # O(1) | If array increased dinamically O(N)
    def enqueue(self, item):
        self.queue.append(item)

    # O(N) -> switch elements to begginning
    def dequeue(self):
        if not self.is_empty():
            item = self.queue[0]
            del self.queue[0]
            return item

    # O(1)
    def peek(self):
        if not self.is_empty():
            return  self.queue[0]

    def __repr__(self):
        return ' '.join((str(elem) for elem in self.queue)) if not self.is_empty() else '--EMPTY QUEUE!--'
