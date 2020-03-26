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

    def middle_ele(self):
        temp = self.head
        count = 0

        while self.head:
            if (count % 2 != 0):
                temp = temp.next
            self.head = self.head.next

            count += 1

        print(temp.data)


llist = LinkedList()
llist.push(1)
llist.push(20)
llist.push(100)
llist.push(15)
llist.push(35)
llist.push(25)
llist.middle_ele()
