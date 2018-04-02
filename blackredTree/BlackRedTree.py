from blackredTree.Node import Node

class BlackRedTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        # Checking if blackredTree properties are violated

        return node



