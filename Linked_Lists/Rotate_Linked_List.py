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

    def rotate(self, k):

        p = self.head
        q = self.head

        prev = None
        count = 0

        # initially we break the linked list at point p which lies at k point from start
        # q is another pointer lying in last node ( remember not null)
        # thus we make sure that p not reaches next node and q not reaching NULL
        # we also track previous value and store both pointers at correct locations
        while p and count < k:
            prev = p
            p = p.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        # end node must point to start i.e head node
        q.next = self.head
        # move head to next node of p pointer
        self.head = p.next
        # when next node is disconnected set p to null
        p.next = None

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
ll.rotate(4)
ll.print_linkedList()
