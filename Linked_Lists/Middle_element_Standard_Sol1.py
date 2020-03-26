class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def push(self, data):

        node = Node(data)
        node.next = self.head
        self.head = node

    def middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while (fast_ptr is not None and fast_ptr.next is not None):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        print(slow_ptr.data)


list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(0)
list1.middle()
