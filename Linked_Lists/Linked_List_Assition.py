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

    def Add_Linked_List(self, head1, head2):
        result = []
        # Why Node is assigned to Node(0)
        # Checkout - https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode
        # Generally in python we use object by reference
        # For every object a unique reference is cerated in heap so when we point to same object i.e Node(0)
        # here we are actually pointing to same reference. So if object state is changed
        # it will be reflected in both references are same if checked in variables.

        node = Node(0)
        p1 = node
        carry = 0
        tmp = p1

        while(True):
            new_sum = 0
            new_sum1 = 0
            new_sum2 = 0
            if head1 is None and head2 is None:
                break
            elif head2:
                new_sum1 = head2.data + carry
                print(head2.data)
                if new_sum > 9:
                    carry = 1
                    new_sum = 0
                    tmp.data = Node(new_sum1)
                    tmp.next = Node(0)
                    tmp = tmp.next
                tmp.data = Node(new_sum1)
                tmp.next = Node(0)
                tmp = tmp.next
                head2 = head2.next

            elif head1:
                new_sum2 = head1.data + carry
                print(head1.data)
                if new_sum > 9:
                    carry = 1
                    new_sum2 = 0
                    tmp.data = Node(new_sum2)
                    tmp.next = Node(0)
                    tmp = tmp.next
                tmp.data = Node(new_sum2)
                tmp.next = Node(0)
                tmp = tmp.next
                head1 = head1.next

            else:
                if head1 and head2:
                    new_sum = head1.data + head2.data + carry
                    if new_sum > 9:
                        carry = 1
                        new_sum = 0
                        tmp.data = Node(new_sum)
                        tmp.next = Node(0)
                        tmp = tmp.next
                tmp.data = Node(new_sum)
                tmp.next = Node(0)
                tmp = tmp.next
                head1 = head1.next
                head2 = head2.next

        print
        while current:

            result.append(current.data)
            current = current.next
        print(result)


llist1 = LinkedList()
llist1.push(3)
llist1.push(4)
llist1.push(5)


llist2 = LinkedList()
llist2.push(4)
llist2.push(5)


a = LinkedList()
a.Add_Linked_List(llist1.head, llist2.head)
