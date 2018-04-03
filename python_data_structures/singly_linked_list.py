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

    def search(self, data):
        """Method to search for a Node containing given data within Singly
        Linked List."""

        # Searching for a Node containing the given data is very similar to
        # deleting a Node containing the give data. All we have to do is 1)
        # create a variable that will represent the Node we're searching for
        # and 2) iterate over our Singly Linked List to return the Node we're
        # searching for (if it exists).

        # Just like we did with delete_node, we should check to ensure that our
        # list isn't empty before proceeding. If it is, we skip right to
        # raising an exception. That check is performed below on line 1.

        if self.head:

            # If the list isn't empty, we can perform the search. First we
            # need to assign a variable with which to traverse our list. Just
            # like in the delete_node method, this variable will assume the
            # identity of each Node in our list until it find the Node we're
            # searching for. That variable is below, on line 159.

            searching_node = self.head

            while searching_node:

                # Now we're in the heart of this method. We begin iterating
                # using a while loop, the goal here being to iterate over every
                # Node until we either find the one we're searching for or hit
                # the end of our list. If we hit the end of our list, the
                # variable searching_node will become None, the while loop will
                # cease it's execution, and the exception will be raised.

                if searching_node.data == data:

                    # We have now found the Node we've been searching for. We
                    # know this because searching_node's data is equal to the
                    # data we gave it (that check is performed above on line
                    # 170). Now we return the Node, accomplished below on line
                    # 178.

                    return searching_node

                searching_node = searching_node.next_node

                # Line 180 above reassigns the variable searching_node to the
                # next Node in our list. We do this continuous reassignment
                # because it is the only way to iterate over our Singly Linked
                # List.

        raise LookupError("""Node containing given data does exist within
                          Singly Linked List.""")

        # And finally, the above will occur if either the list is empty or the
        # list doesn't contain a Node with the given data. This is, again, not
        # necessary.

    def pop(self):
        """Method to delete and return list's head."""

        # Just like we've done in previous methods, we're first going to check
        # to ensure the list isn't empty by ensuring it has a head. We do this
        # below on line 201.

        if self.head:

            # As we did in the delete_node method, when it turned out the Node
            # we wanted to delete was the head Node, all we have to do is
            # reassign the head to become it's next_node. The only difference
            # is that we first assign a variable to be the head Node's data so
            # that we can return it after it has been reassigned. These steps
            # are performed on the three lines below.

            head_data = self.head.data
            self.head = self.head.next_node
            return head_data

        raise IndexError("""Cannot pop from an empty list.""")

        # Above we raise an exception, only this time it's an IndexError
        # instead of a LookupError (since we're not actually 'looking' for
        # anything, just removing the head Node if it's there). This error will
        # only get raised if the Singly Linked List is empty.

    def display(self):
        """Method to display the current state of the list."""

        # In order to display our Singly Linked List, we first need to define a
        # variable with which to hold our list's Node data. The plan is to
        # continuously add to this variable for every Node in our list and then
        # return it once we've reached the end. The visual representation of a
        # Node in our list will have square brackets (which represent the Node)
        # the data within the square brackets (which represent the data that
        # each Node holds), and a text-based arrow pointing to the right (which
        # will represent the Node's next_node pointer).

        # The variable mentioned above is defined below on line 244, called
        # all_nodes. An important thing to note here is that all_nodes is
        # initially an empty list. You may be asking yourself "why not make it
        # an empty string and use string concatenation to add the Node data?".
        # That's a great question. The answer is that string concatenation in
        # Python is an O(n^2) operation, an inefficient time complexity
        # considering the simple nature of our task. To circumnavigate this
        # issue, one can simply append string elements to an empty list and
        # return a ''.join() on that list instead. The end result is the same
        # and the time complexity is dropped to O(n), which is much better.

        all_nodes = []

        # Now we must do as we've done in previous methods, which is to iterate
        # over the Singly Linked List. To do this we first define a variable
        # below called current_node. This variable will take the form of every
        # Node in our list as we iterate over it.

        current_node = self.head

        while current_node:

            # We're now iterating over our list, appending the correct strings
            # in the correct order to properly display the Singly Linked List.
            # Note that below we must first use the str() method on our data.
            # This only needs to happen if current_node.data isn't inherently a
            # string.

            all_nodes.append('[ ' + str(current_node.data) + ' ]' + ' -> ')

            # As we've done plenty of times by now, we then reassign
            # current_node to become it's next_node to continue iteration. This
            # is accomplished below, on line 267.

            current_node = current_node.next_node

        # Now that we're done iterating, we know we've reached the end of our
        # Singly Linked List. All data from all Nodes has been properly stored
        # and is ready to be returned. The final step we must take before
        # returning that data is to append one final string of 'None' which
        # represents the end of our list. We do this below on line 275.

        all_nodes.append('None')

        # We did it! Now we use ''.join(), passing in the all_nodes variable,
        # to return the visual representation of our Singly Linked List!

        return ''.join(all_nodes)
