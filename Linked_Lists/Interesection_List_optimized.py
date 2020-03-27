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

    def getSize(self, head):
        count = 0
        curr_node = head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def intersetPoint(self, head_a, head_b):
        sz_a = self.getSize(head_a)
        sz_b = self.getSize(head_b)

        # difference between the two lists size
        diff = abs(sz_a-sz_b)

        curr_a = head_a
        curr_b = head_b
        if sz_b < sz_a:
            for i in range(diff):
                curr_a = curr_a.next
        else:
            for i in range(diff):
                curr_b = curr_b.next

        while curr_a != curr_b:
            curr_b = curr_b.next
            curr_a = curr_a.next

        if curr_a and curr_b:
            return curr_a.data
        else:
            return -1

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
llist2.push(9)
llist2.push(10)


a = LinkedList()
print("Initial Linked ")
llist1.print_linkedList()
llist2.print_linkedList()
print("--------------------")
print(a.intersetPoint(llist1.head, llist2.head))
