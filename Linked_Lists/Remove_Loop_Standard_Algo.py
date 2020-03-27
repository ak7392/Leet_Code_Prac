class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
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

    def remove_loop(self):

        p = self.head
        q = self.head

        while p != q.next:
            p = p.next
            q = q.next
        p.next = None

    def detect_loop(self):

        p = self.head
        q = self.head

        while p and q and q.next:
            p = p.next
            q = q.next.next

            if p == q:
                print(True)
                return

    def print_ll(self):

        result = []
        current = self.head

        while current != None:

            result.append(current.data)
            current = current.next
        print(result)


llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.print_ll()
llist.head.next.next.next.next = llist.head
llist.remove_loop()
llist.detect_loop()
