from LinkedList.singly_linked_list.singly_linked_list import SinglyLinkedList

lst = SinglyLinkedList()
assert lst.length == 0
lst.add_to_head('a')
assert lst.length == 1
assert lst.display() == 'a'
lst.add_to_head('b')
assert lst.display() == 'b,a'
lst.add_to_tail('c')
assert lst.display() == 'b,a,c'
lst.remove_from_head()
assert lst.length == 2
assert lst.display() == 'a,c'


lst = SinglyLinkedList()
lst.remove_from_head()
assert lst.length == 0
lst.add_to_tail('a')
assert lst.display() == 'a'
assert lst.length == 1
lst.remove_from_tail()
assert lst.length == 0
lst.add_to_head('d')
lst.add_to_tail('e')
lst.add_to_head('f')
assert lst.display() == 'f,d,e'
lst.remove_from_tail()
assert lst.display() == 'f,d'
assert lst.find("f") is not None
assert lst.find("g") is None


