from heap.Node import Node

class MaxHeap(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not None:
            return Node(data)

        if not node.left_child:
            node.left_child = self.insertNode(data, node.left_child)
        elif not node.right_child:
            node.right_child = self.insertNode(data, node.right_child)

        pass

    # root -> O(Log N), airbitrary node -> O(N)
    def delete(self, data):
        # delete node, check heap validity and reconstruct if properties are violated
        pass

    # O(Log N)
    def getMax(self):
        # return and delete root node and reconstruct the tree
        pass