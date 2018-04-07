"""Module to implement Doubly Linked List in Python."""


class Node(object):
    """Class to create instance of Node."""

    def __init__(self, data, next_node=None, prev_node=None):
        """Create new instance of Node class object."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList(object):
    """Class to create instance of Doubly Linked List."""

    def __init__(self):
        """Create new instance of DoublyLinkedList class object."""
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Method to add new Node to Doubly Linked List."""

        # Overview:
        # The manner in which we add a new Node to a DoublyLinkedList is very
        # similar to how we add a new Node in a SinglyLinkedList, with a few
        # key differences that I'll point out as we go. The first thing we do
        # is create a variable to become the list's current head. We then
        # reassign the list's head to become a new Node who's next_node
        # is the variable we created. The new Node is now the head, and the old
        # head (which is the variable we defined) is now the new Node's
        # next_node, thus adding to our list. Next, since a DoublyLinkedList
        # contains Nodes which have prev_node pointers, as well as a tail, we
        # must add further logic that accounts for that.

        # On line 43 below, we create a variable called new_next_node to become
        # the current head of the DoublyLinkedList. Then, on line 44, we
        # reassign the head of the list to become a new Node who's next_node
        # pointer is the old head, which is the variable new_next_node. This is
        # exactly what we did in the SinglyLinkedList.

        new_next_node = self.head
        self.head = Node(data, new_next_node)

        # Since this is a DoublyLinkedList it must have a tail. The tail should
        # always be the very last Node of the list, which also happens to be
        # the very first Node added to the list. In order for us to properly
        # handle the assignment of the list's tail we first need to check if
        # the list only has one Node (which is the Node we just added). We
        # perform this check below on line 53.

        if not self.head.next_node:

            # If the list only has one Node, we can proceed to assign the tail.
            # We do this below on line 70 by making the tail equal the head of
            # the list. Now, I know what some of you may be thinking. If the
            # head of the list and the tail of the list are opposite of one
            # another, why would we make the tail equal the head? That's a
            # great question! The answer lies in the way we've set up our logic
            # up to this point in the method. Every Node we add takes the place
            # of the list's head, ensuring that the head is continuously
            # reassigned. The tail, however, only has to be worried about once
            # when we're adding the first Node to the list. By making the tail
            # equal to the very first Node added, we've ensured that the tail
            # will stay in it's rightful place at the end of the list and that
            # the head can continue getting reassigned without effecting the
            # tail.

            self.tail = self.head

        else:

            # If the list contains more than one Node, the only other thing we
            # need to do is give the new_next_node variable a prev_node that
            # points to the new head of the list. By doing this for every new
            # Node we add, we ensure that every Node has a pointer to the Node
            # directly behind it in the DoublyLinkedList.

            new_next_node.prev_node = self.head

    def delete_node(self, data):
        """Method to delete first Node found containing given data, starting
        from head."""

        # OVERVIEW
        # Deleting a Node in a DoublyLinkedList is similar to how we delete a
        # Node from a Singly Linked List, with a few extra steps to ensure all
        # Nodes are appropriately assigned. After making sure our list isn't
        # empty, we then check to see if the Node we want to delete is the head
        # of our list.

        if self.head:

            if self.head.data == data:

                if self.head.next_node:

                    self.head = self.head.next_node
                    self.head.prev_node = None

                else:

                    self.head = None
                    self.tail = None

                return 'Node has been deleted.'

            current_node = self.head

            while current_node:

                if current_node.data == data:

                    if current_node is self.tail:

                        self.tail = current_node.prev_node
                        self.tail.next_node = None

                    else:

                        current_node.prev_node.next_node = current_node.next_node
                        current_node.next_node.prev_node = current_node.prev_node

                    return 'Node has been deleted.'

                current_node = current_node.next_node

        raise LookupError("""No Node containing given value exists in Doubly
                          Linked List.""")
