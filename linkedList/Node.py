class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def remove(self, data, previous_node):
        if self.data == data:
            previous_node.next = self.next
            del self.data
            del self.next
        else:
            self.next.remove(data, self)
