
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class CircularLinkedList(object):
    import sys

    def __init__(self, head=None, end=None):
        '''
            Initalize a linke list with a head and a tail.
        '''

        self.head = head
        self.end = end

    def traverse(self):
        '''
            Traverse the list and print each value.
            Time Complexity: O(n)
        '''

        # define the first node
        curr_node = self.head

        # as long as there is a next node, keep going
        while curr_node.next_node:

            # print the data
            print(curr_node.data)

            # reassign the next node
            curr_node = curr_node.next_node

            # here is the issue, if we don't add this condition we get an ifinite loop.
            # Once the current node is the head again, then exit the loop.
            if curr_node == self.head:
                break

    def insert_end(self, data):
        '''
            Insert a node at the end of our linked list.
            Time Complexity: O(1)
        '''

        new_node = Node(data)

        # handle empty list case
        if self.head == None:
            self.head = new_node
            self.head.next_node = new_node
            self.end = new_node
            return

        # handle non-empty list case
        if self.end != None:
            self.end.next_node = new_node
            new_node.next_node = self.head
            self.end = new_node
            return

    def insert_beg(self, data):
        '''
            Insert a node at the beginning of our linked list.
            Time Complexity: O(1)
        '''

        new_node = Node(data)
        new_node.next_node = self.head
        curr_node = self.head

        # handle empty list case
        if curr_node == None:
            self.head = new_node
            self.end = new_node
            self.head.next_node = new_node
            return

        # handle non-empty list case
        if self.end != None:
            self.end.next_node = new_node
            new_node.next_node = self.head
            self.head = new_node
            return

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next_node
            cur.next_node = self.head.next_node
            self.head = self.head.next_node
        else:
            cur = self.head
            prev = None
            while cur.next_node != self.head:
                prev = cur
                cur = cur.next_node
                if cur == node:
                    prev.next_node = cur.next_node
                    cur = cur.next_node

    def Josephus(self, step):
        cur = self.head
        print(self)
        # while len(self) > 1:

        # while len(self) > 1:
        while cur
        count = 1
        while count != step:
            cur = cur.next_node
            count += 1
        print("REMOVED"+"-"+str(cur.data)+"th DataNode")
        self.remove_node(cur)
        cur = cur.next_node


circular = CircularLinkedList()

circular.insert_end(59)
circular.insert_end(49)
circular.insert_end(51)

circular.insert_beg(52)
circular.Josephus(2)

print(circular.traverse())
