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

    # d --> 6 --> 8 --> 12 --> 15

    def swap_elements(self):
        result = []

        # Reference will change as we move on list while swapping elements
        # Just to make sure we don't need to make initializations we consider taking reference inside another
        # variable just to make sure it points to updated state of object
        # In python we genrally use object by reference
        d1 = d = Node(0)
        d.next = self.head

        while d.next and d.next.next:
            #    1      2   3
            # d --> 6 --> 8 --> 12 --> 15
            # d     p     q
            p = d.next
            q = d.next.next
            # we have to tranform it to
            #   2
            # d --> 8 --> 6 --> 12 --> 15
            # We have to modify 1,2,3 references in below fashion:
            d.next, p.next, q.next = q, q.next, p
            # Now since we have to swap next two elements we can consider d element at 6th node
            # Since 6th node is already swapped we can place d pointer there
            # d --> 8 --> 6 --> 12 --> 15 --> 18
            #              d     p      q
            d = p

        # Starting from head of new swapped List and Iterating over till None
        current = d1.next
        while current != None:

            result.append(current.data)
            current = current.next
        print(result)


llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)

print(llist.swap_elements())
