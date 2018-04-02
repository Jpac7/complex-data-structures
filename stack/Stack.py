class Stack(object):
    # THE ABSTRACT DATA TYPE CAN BE IMPLEMENTED WITH ARRAY OR LINKED LIST
    # HERE, IS IMPLEMENTED WITH AN ARRAY

    def __init__(self):
        self.stack = []
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    # O(1)
    def push(self, item):
        self.length += 1
        self.stack.append(item)

    # O(1)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    # O(1)
    def pop(self):
        if not self.is_empty():
            self.length -= 1
            item = self.stack[-1]
            del self.stack[-1]
            return item
