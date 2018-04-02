from avlTree.Node import Node

class AVLTree(object):

    def __init__(self):
        self.root = None

    # O(Log N)
    def insert(self, data):
        print('Insert {}'.format(data))
        self.root = self.insert_node(data, self.root)
        

    def insert_node(self, data, node):
        if not node:
            return Node(data)
        
        # insert node
        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)
        
        # Update the new node height
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        
        # check if tree is balanced
        # if not, rotate until it gets balanced
        return self.balance_tree(node, data)
        
    def balance_tree(self, node, data):

        # If height_diff > 1 or <-1 the node subtrees are unbalanced
        subtrees_height_diff = self.calc_balance(node)

        # Case 1 - doubly left heavy situation
        if subtrees_height_diff > 1 and data < node.left_child.data:
            print("Doubly left heavy situation")
            return self.rotate_right(node)

        # Case 2 - doubly right heavy situation
        if subtrees_height_diff < -1 and data > node.right_child.data:
            print("Doubly right heavy situation")
            return self.rotate_left(node)

        # Case 3 - left right heavy situation
        if subtrees_height_diff > 1 and data > node.left_child.data:
            print("Left right heavy situation")
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        # Case 4 - right left heavy situation
        if subtrees_height_diff < -1 and data < node.right_child.data:
            print("Right left heavy situation")
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def calc_height(self, node):
        if not node:
            return -1

        return node.height

    def calc_balance(self, node):
        """
        Calculate if node's left subtree and right subtree are balanced
        :param node: The node to calculate the difference of heights between subtrees
        :return: the difference value between the heights of left and right subtrees. for >0 value, left subtree is bigger
        than right subtree..
        """
        if not node:
           return 0

        return self.calc_height(node.left_child) - self.calc_height(node.right_child)

    # O(1)
    def rotate_right(self, node):
        print("Rotating right on node {}".format(node.data))
        temp_left_child = node.left_child
        t = temp_left_child.right_child

        temp_left_child.right_child = node
        node.left_child = t

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_left_child.height = max(self.calc_height(temp_left_child.left_child), self.calc_height(temp_left_child.right_child)) + 1

        return temp_left_child

    # O(1)
    def rotate_left(self, node):
        print("Rotating left on node {}".format(node.data))
        temp_right_child = node.right_child
        t = temp_right_child.left_child

        temp_right_child.left_child = node
        node.right_child = t

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_right_child.height = max(self.calc_height(temp_right_child.left_child),
                                      self.calc_height(temp_right_child.right_child)) + 1

        return temp_right_child

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print('{}'.format(node.data))

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def delete(self, data):
        if self.root:
            self.root = self._delete_node(data, self.root)

    def _delete_node(self, data, node):

        if not node:
            print("Data not found in structure...")
            return node

        if node.data == data:
            print('Removing node {}'.format(node.data))

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
            node.left_child = self._delete_node(data, node.left_child)

        # Return to the parent node of the removed one to check balance
        if not node:
            return node

        # Checking if the tree gets unbalanced after removal
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1

        balance = self.calc_balance(node)

        # Doubly left heavy situation
        if balance > 1 and self.calc_balance(node.left_child) >= 0:
            print("Doubly left heavy situation")
            return self.rotate_right(node)

        # Left right heavy situation
        if balance > 1 and self.calc_balance(node.left_child) < 0:
            print("Left right heavy situation")
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        # Doubly right heavy situation
        if balance < -1 and self.calc_balance(node.right_child) <= 0:
            print("Doubly right heavy situation")
            return self.rotate_left(node)

        # Right left heavy situation
        if balance < -1 and self.calc_balance(node.right_child) > 0:
            print("Right left heavy situation")
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def find_sucessor(self, node):
        if node.left_child:
            return self.find_sucessor(node.left_child)

        return node

    @classmethod
    def avl_sort(cls, data_array):
        """
        Use AVL sort - O(N * Log N) time complexity
        :param data_array: values stored to sort - O(N) memory complexity
        :return: an avl tree ready for in-order traversal
        """
        pass
