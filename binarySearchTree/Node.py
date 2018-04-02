class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return '<Node data: {}, Left child: {}, Right child: {}>'.format(self.data, self.left_child, self.right_child)
