class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


def new_node(data):
    return Node(data)


class LinkedList():

    def Flatten_Multilevel_Linked_List(self, head):
        if head is None:
            return

        # reaching the tail of first level Linked List
        temp = head
        while temp.next != None:
            temp = temp.next
        current = head

        while current != temp:

            # In case any child node is present
            if current.child:

                # Update the child node at the end of the current list
                temp.next = current.child

                # tmp
                tmp = current.child
                while tmp.next:
                    tmp = tmp.next
                temp = tmp

            current = current.next

    def print_ll(self, head):

        result = []
        if not head:
            return
        while head:
            result.append(head.data)
            head = head.next
        print(result)


if __name__ == '__main__':

    # Child list of 13
    child13 = new_node(16)
    child13.child = new_node(3)

    # Child List of 10
    head1 = new_node(4)
    head1.next = new_node(20)
    head1.next.child = new_node(2)  # Child of 20
    head1.next.next = new_node(13)
    head1.next.next.child = child13

    # Child of 9
    child9 = new_node(19)
    child9.next = new_node(15)

    # Child List of 17
    child17 = new_node(9)
    child17.next = new_node(8)
    child17.child = child9

    # Child List of 7
    head2 = new_node(17)
    head2.next = new_node(6)
    head2.child = child17

    # Main List
    head = new_node(10)
    head.child = head1
    head.next = new_node(5)
    head.next.next = new_node(12)
    head.next.next.next = new_node(7)
    head.next.next.next.child = head2
    head.next.next.next.next = new_node(11)

    a = LinkedList()
    a.Flatten_Multilevel_Linked_List(head)
    a.print_ll(head)
