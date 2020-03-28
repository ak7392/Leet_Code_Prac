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

    def Merge_Linked_List(self, head1, head2):
        result = []
        # Why Node is assigned to Node(0)
        # Checkout - https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode
        # Generally in python we use object by reference
        # For every object a unique reference is cerated in heap so when we point to same object i.e Node(0)
        # here we are actually pointing to same reference. So if object state is changed
        # it will be reflected in both references are same if checked in variables.

        node = Node(0)
        p1 = node
        while(True):
            if head1 is None and head2 is None:
                break
            elif head1 is None:
                p1.next = head2
                break
            elif head2 is None:
                p1.next = head1
                break
            else:
                smaller_val = 0
                if head1.data < head2.data:
                    smaller_val = head1.data
                    head1 = head1.next
                else:
                    smaller_val = head2.data
                    head2 = head2.next

                new_node = Node(smaller_val)
                p1.next = new_node
                p1 = p1.next

        current = node.next
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
llist2.push(1)
llist2.push(12)
llist2.push(18)
llist2.push(11)


a = LinkedList()
print("--------------------")
print(a.Merge_Linked_List(llist1.head, llist2.head))
