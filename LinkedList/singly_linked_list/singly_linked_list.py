from LinkedList.node import Node

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    @property
    def length(self):
        count = 0
        current = self.head

        while(current):
            count += 1
            current = current.next
            
        return count

    def display(self):
        current = self.head
        lst = []
        while(current):
            lst.append(current.item)
            current = current.next

        return ','.join(lst)

    def add_to_head(self, item):
        new_node = Node()
        new_node.item = item

        if not self.head:
            self.head = new_node
        else:
            old_head = self.head
            new_node.next = old_head
            self.head = new_node

    def add_to_tail(self, item):
        if not self.head:
            return self.add_to_head(item)

        current = self.head
        old_tail = current

        while(current):
            old_tail = current
            current = current.next

        new_tail = Node()
        new_tail.item = item
        old_tail.next = new_tail


    def remove_from_head(self):
        if not self.head:
            return

        old_head = self.head
        self.head= old_head.next
        return old_head

    def remove_from_tail(self):
        current = self.head
        old_previous = self.head
        if not self.head:
            return
        elif self.length == 1:
            return self.remove_from_head()

        while(current and current.next):
            old_previous = current
            current = current.next

        old_previous.next = None
        return current


    def find(self, item):
        current = self.head
        if not self.head:
            return None

        while(current):
            if current.item == item:
                return current
            else:
                current = current.next
        return None



