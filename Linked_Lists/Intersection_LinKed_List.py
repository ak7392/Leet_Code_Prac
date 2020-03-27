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

    def Intersection_lls(self, head1, head2):
        current1 = head1
        current2 = head2

        while current1 != current2:

            if current1:
                current1 = current1.next
            current1 = head2

            if current2:
                current2 = current2.next
            current2 = head2

        return current1.data

    def print_linkedList(self):

        result = []
        current = self.head

        while current != None:

            result.append(current.data)
            current = current.next
        print(result)


llist1 = LinkedList()
llist1.push(9)
llist1.push(8)
llist1.push(7)
llist1.push(6)
llist1.push(5)
llist1.push(4)
llist1.push(3)
llist1.push(2)

llist2 = LinkedList()
llist2.push(6)
llist2.push(5)
llist2.push(4)


a = LinkedList()
print("Initial Linked ")
llist1.print_linkedList()
llist2.print_linkedList()
print("--------------------")
print(a.Intersection_lls(llist1.head, llist2.head))
