"""Module to implement Singly Linked List in Python."""


class Node(object):
    """Class to create instance of Node."""

    def __init__(self, data=None, next_node=None):
        """Create new intance of a Node class object."""

        self.data = data
        self.next_node = next_node


class SinglyLinkedList(object):
    """Class to create instance of Singly Linked List."""

    def __init__(self):
        """Create new instance of a Singly Linked List class object."""

        self.head = None

    def add_node(self, data):
        """Method to add new Node to Singly Linked List."""

        # When we want to add a new Node to our Singly Linked List, all we have
        # to do is 1) create a variable that contains the current list's head
        # Node and 2) reassign the list's head Node to become a new instance
        # of our Node class.

        new_next_node = self.head

        # 1) On line 31 we create a new variable called new_next_node
        # and assign it's value to the list's current self.head. We'll then use
        # this variable below on step 2.

        self.head = Node(data, new_next_node)

        # 2) On line 37 we reassign the list's head Node to become the newly
        # added Node. It's data will be the data passed in as the
        # argument for our method and it's next_node will become what the old
        # head Node used to be.

    def delete_node(self, data):
        """Method to delete a Node in the Singly Linked List with the given
        data."""

        # Below, on line 49, we check to make sure our Singly Linked List is
        # not empty. If it isn't, we proceed with further checks, and if it is,
        # we skip down to raising an exception.

        if self.head:

            # Before we go assigning variables and iterating over Nodes in our
            # list, we can always do a quick check to make sure that the Node
            # to be deleted isn't the list's head Node. We check this on line
            # 58.

            if self.head.data == data:

                # If it turns out that the Node we want to delete is indeed the
                # list's head Node, all we have to do is reassign the head of
                # our list to become the current head Node's next_node. Then,
                # we return the data to signify that the Node has been deleted.

                self.head = self.head.next_node
                return data

            # If the head Node isn't the Node we want to delete, we must 1)
            # assign variables that represent different points in our
            # Singly Linked List, 2) iterate over the Singly Linked List
            # looking for the Node we want to delete, 3) delete the Node
            # we've been looking for.

            node_to_be_deleted = self.head
            previous_node = self.head

            # 1)
            # On lines 74 and 75 above, we assign two variables that will
            # represent two points in our Singly Linked List. The first,
            # node_to_be_deleted, will eventually be the Node we delete
            # from our Singly Linked List. The second, previous_node, will
            # be the Node just before the Node we end up deleting.

            while node_to_be_deleted:

                # 2)
                # On line 84, we begin iterating over our Singly Linked
                # List. We specify that while node_to_be_deleted, that is,
                # while it still has some truthy non-None value, we will
                # continue iterating. We do this because as soon as we hit
                # the end of the list, node_to_be_deleted will become None,
                # which indicates that we've iterated over the entire list.

                if node_to_be_deleted.data == data:

                    # 3)
                    # We've finally found the Node we want to delete! In
                    # order to delete this Node from our Singly Linked
                    # List, all we have to do is assign previous_node's
                    # next_node to become node_to_be_deleted's next_node.
                    # We do this because, in Python, objects that are no
                    # longer referenced in memory are 'garbage-collected',
                    # or deleted. In order to delete a Node, we just ensure
                    # that nothing points to that Node. Simple!

                    # This is also the reason why we created the two
                    # variables on lines 74 and 75. The variable
                    # node_to_be_deleted served to eventually land on the
                    # Node we want to delete, consistently checking the
                    # data of the Nodes as our while loop iterates. The
                    # other variable, previous_node, serves by being one
                    # Node prior to node_to_be_deleted so that when
                    # node_to_be_deleted eventually lands on the Node we
                    # wish to delete all we have to do is reassign
                    # previous_node's next_node. This reassignment happens
                    # below, on line 118.

                    previous_node.next_node = node_to_be_deleted.next_node
                    return data

                previous_node = node_to_be_deleted
                node_to_be_deleted = node_to_be_deleted.next_node

                # Lines 121 and 122 above are to ensure that our
                # variables get reassigned to the correct Nodes down
                # our list if we haven't yet found the Node we want to
                # delete.

        raise LookupError("""A Node with the given data does not exist in the
                          Singly Linked List.""")

        # Line 129 will raise a LookupError if the given value to delete does
        # not exist in any Node within our Singly Linked List. That is to say,
        # if the Node the user input isn't in our list, we tell them! It should
        # be noted that raising an error is not necessary.
