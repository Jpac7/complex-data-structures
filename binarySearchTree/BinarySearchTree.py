from binarySearchTree.Node import Node


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def get_height(self):
        pass

    def insert(self, data):
        # Tree is empty
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(data, self.root)

    # O(Log N)
    def _insert_node(self, data, node):
        if data < node.data:
            if node.left_child:
                self._insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
                print("inserted as left child: {}".format(data))
        else:
            if node.right_child:
                self._insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)
                print("inserted as right child: {}".format(data))

    # O(Log N)
    def get_min(self):
        if self.root:
            return self._min(self.root)

    def _min(self, node=None):

        if node.left_child:
            return self._min(node.left_child)

        return node.data

    # O(Log N)
    def get_max(self):
        if self.root:
            return self._max(self.root)

    def _max(self, node=None):

        if node.right_child:
            return self._max(node.right_child)

        return node.data

    # O(N)
    def tranverse(self):
        if self.root:
            self._tranverse_in_order(self.root)

    def _tranverse_in_order(self, subtree_root):
        """
         In-order Traversal of the binary search tree
         :return: Numerical/Alphabetic Ordering of tree elements
         """

        if subtree_root.left_child:
            self._tranverse_in_order(subtree_root.left_child)

        print(subtree_root.data)

        if subtree_root.right_child:
            self._tranverse_in_order(subtree_root.right_child)

    # O (Log N)
    def delete(self, data):
        if self.root:
            self.root = self._delete_node(data, self.root)

    def _delete_node(self, data, node):

        if not node:
            print("Data not found in structure...")
            return node

        if node.data == data:

            if not node.left_child and not node.right_child:
                print("Removing a leaf node...")
                del node
                return None

            if not node.left_child:
                print("Removing a node with single right child...")
                tmp_node = node.right_child
                del node
                return tmp_node
            elif not node.right_child:
                print("Removing a node with single left child...")
                tmp_node = node.left_child
                del node
                return tmp_node

            print("Removing a node with two children...")
            sucessor_node = self.find_sucessor(node.right_child)
            node.data = sucessor_node.data
            node.right_child = self._delete_node(sucessor_node.data, node.right_child)

        elif data > node.data:
            node.right_child = self._delete_node(data, node.right_child)
        else:
            self._delete_node(data, node.left_child)

        return node

    def find_sucessor(self, node):
        if node.left_child:
            return self.find_sucessor(node.left_child)

        return node
