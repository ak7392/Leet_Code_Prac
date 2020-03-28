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

    def Check_Palindorme(self):
        # Method1
        # string = ''
        # current = self.head

        # while current:

        #     string += current.data
        #     current = current.next

        # return string == string[::-1]

        # Method2
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head

        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True


llist = LinkedList()
llist.push('R')
llist.push('A')
llist.push('D')
llist.push('A')
llist.push('R')

llist2 = LinkedList()
llist2.push('A')
llist2.push('N')
llist2.push('N')


print(llist.Check_Palindorme())
print(llist2.Check_Palindorme())
