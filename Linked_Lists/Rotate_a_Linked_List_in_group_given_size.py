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

    def rotate_in_groupsizes(self, head, k):
        current = head
        nxt = None
        prev = None
        count = 0

        while current is not None and count < k:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1

        if nxt is not None:
            head.next = self.rotate_in_groupsizes(nxt, k)

        return prev

    def print_linkedList(self):

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
llist.print_linkedList()
llist.head = llist.rotate_in_groupsizes(llist.head, 3)
llist.print_linkedList()
