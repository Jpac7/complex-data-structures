from linkedList.LinkedList import LinkedList

linked_list = LinkedList()

linked_list.insertEnd(44)
linked_list.insertEnd(2)
linked_list.insertEnd(99)
linked_list.insertStart(100)

linked_list.tranverse()
print("Size: {}".format(linked_list.size()))

linked_list.remove(2)

linked_list.tranverse()
print("Size: {}".format(linked_list.size()))

linked_list.remove(100)

linked_list.tranverse()
print("Size: {}".format(linked_list.size()))
