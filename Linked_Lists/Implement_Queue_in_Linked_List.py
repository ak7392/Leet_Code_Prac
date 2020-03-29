class IsEmptyString(IsADirectoryError):
    pass


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def len(self):
        return self.size == 0

    def top(self):
        return self.head.data

    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IsEmptyString("This LinkedList is empty")
        result = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.isEmpty():
            self.tail = None

        return result


llist = LinkedList()
llist.enqueue(9)
llist.enqueue(8)
llist.enqueue(7)
llist.enqueue(6)
llist.enqueue(5)
llist.enqueue(4)
llist.enqueue(3)


print(llist.dequeue())
print(llist.top())
