class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
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

    def cal_size(self):

        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def Nth_element(self, n):

        current = self.head
        front_cnt = self.cal_size() - n
        print(front_cnt)

        while front_cnt > 0:

            current = current.next
            front_cnt -= 1
        return current.data

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
llist.push(5)
llist.push(4)
llist.push(3)

llist.print_ll()
print(llist.Nth_element(2))
