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

    def detect_loop(self):

        s = set()
        temp = self.head

        while temp is not None:

            # If we have already has
            # this node in hashmap it
            # means their is a cycle
            # (Because you we encountering
            # the node second time).
            if temp in s:
                return True

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
            temp = temp.next

        return False

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
# Creating Loop on Linked List for testing
llist.head.next.next.next.next = llist.head
print(llist.detect_loop())
