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

    def Add_Lists(self, head1, head2):
        p = head1
        q = head2
        carry = 0
        temp = None
        prev = None
        result = []

        while p or q:
            if p is None:
                i = 0
            else:
                i = p.data
            if q is None:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                s = s % 10

            else:
                carry = 0

            temp = Node(s)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)

    # def print_linkedList(self):

    #     result = []
    #     current = self.head

    #     while current != None:

    #         result.append(current.data)
    #         current = current.next
    #     print(result)


llist1 = LinkedList()
llist1.push(9)
llist1.push(8)
llist1.push(7)


llist2 = LinkedList()
llist2.push(6)
llist2.push(5)
llist2.push(4)


a = LinkedList()
print(a.Add_Lists(llist1.head, llist2.head))
