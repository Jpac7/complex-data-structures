class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0

    def __repr__(self):
        return str(self.data)

