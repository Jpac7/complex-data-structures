from linkedList.Node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    # O(1)
    def insertStart(self, data):
        self.counter += 1

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # O(N)
    def insertEnd(self, data):
        self.counter += 1

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        actual_node = self.head

        while actual_node.next is not None:
            actual_node = actual_node.next

        actual_node.next = new_node

    # O(N)
    def tranverse(self):
        actual_node = self.head

        while actual_node is not None:
            print("{}".format(actual_node.data))
            actual_node = actual_node.next

    # O(N) at Max
    def remove(self, data):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
            else:
                self.head.next.remove(data, self.head)

            self.counter -= 1

    # O(1)
    def size(self):
        return self.counter
