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

    def reverse_link(self):

        nxt = None
        prev = None
        current = self.head

        while current != None:

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def print_linkedList(self):

        result = []
        current = self.head

        while current != None:

            result.append(current.data)
            current = current.next
        print(result)


ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(85)
ll.print_linkedList()
ll.reverse_link()
ll.print_linkedList()
