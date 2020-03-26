class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class middle_element():

    def __init__(self):
        self.head = None
        self.end = None

    def insert_beg(self, data):
        '''
            Insert a node at the beginning of our linked list.
            Time Complexity: O(1)
        '''

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def find_length(self):

        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def find_middle(self, count):

        curr = self.head

        new_count = 0

        while new_count < count//2:

            curr = curr.next
            new_count += 1

        print(curr.data)


a = middle_element()
a.insert_beg(1)
a.insert_beg(2)
a.insert_beg(3)
a.insert_beg(4)
a.insert_beg(5)
a.insert_beg(6)
count = a.find_length()
print(a.find_middle(count))
