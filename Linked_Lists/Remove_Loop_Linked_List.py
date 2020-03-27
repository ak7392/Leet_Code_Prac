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

    def Linked_List_with_Loop(self):

        current = self.head
        prev = None

        while current != None:
            prev = current
            current = current.next

        prev.next = self.head

    def remove_loop(self):

        p = self.head
        q = self.head

        while p and q and q.next:
            p = p.next
            q = q.next.next

            if p == q:
                p.next.next = None
                return

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
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_ll()
llist.Linked_List_with_Loop()
llist.remove_loop()
llist.detect_loop()
