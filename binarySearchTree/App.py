from binarySearchTree.BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

bst.insert(50)
bst.insert(5)
bst.insert(20)
bst.insert(70)
bst.insert(80)
bst.insert(10)

bst.tranverse()

print('BST min: %s' % (str(bst.get_min())))
print('BST max: %s' % (str(bst.get_max())))

bst.delete(50)
bst.tranverse()

print("Root: %s" % bst.root.data)

