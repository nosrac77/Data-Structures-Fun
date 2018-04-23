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
        # Nodes are appropriately assigned. The relevant differences to be
        # aware of are 1) that Nodes here have a new property prev_node
        # pointer to the Node just before it in the list, and 2) that the list
        # has a tail Node that always resides at the end of the list.

        if self.head:

            # The first check is to ensure that the list is not empty by
            # ensuring that it has a head. We do this above on line 94.

            if self.head.data == data:

                # The check above only activates if the head Node happens to be
                # the Node we're seeking to delete from the list. If it is, we
                # must then check to see if the list is only comprised of one
                # Node. If there's only one Node in the list, we have to
                # perform a different action than if the Node has a neighbor.

                if self.head.next_node:

                    # To recap, if the Node we're trying to delete is the head
                    # of our DoublyLinkedList and it also has at least one
                    # other Node beside it in the list, we land here. We then
                    # reassign the head to become it's next_node, which we do
                    # below on line 118. Since the head has been reassigned,
                    # the only other step is to reassign the new head's
                    # prev_node pointer to be None (line 119 below). The Node
                    # is now deleted!

                    self.head = self.head.next_node
                    self.head.prev_node = None

                else:

                    # If the Node we want to delete is the head Node, and the
                    # list only contains one Node, we land here. Deleting a
                    # Node in this case is relatively straight-forward.
                    # Reassigning both the list's head and the tail to None
                    # will do the job (lines 129 and 130 below).

                    self.head = None
                    self.tail = None

                # In either case, the head Node will be deleted. The return
                # statement below is to ensure that the method ceases it's
                # execution and informs the user that the operation was
                # successful.

                return 'Node has been deleted.'

            # If the Node we wish to delete is not the list's head, we must
            # iterate through the list in order to find it. Keen observers may
            # already be asking themselves "Before iterating, shouldn't we do a
            # check to see if the Node we want to delete is the list's tail?".
            # This is a great question. The reason we're iterating first and
            # adding logic to check the tail later is due to the nature of our
            # method. It's purpose is to delete the first Node containing the
            # given data. If we immediately check the tail, we may skip a Node
            # that contains the given data and thus violate the purpose of our
            # method.

            # Below we assign a variable called current_node which we'll use to
            # iterate over our list in search of the Node we wish to delete. In
            # the same way we've done before, we'll then use a while loop to
            # continuously reassign current_node until it becomes the Node we
            # wish to delete.

            current_node = self.head

            while current_node:

                if current_node.data == data:

                    # If we've finally found the Node we want to delete, we
                    # first check to ensure that it's not the list's tail. If
                    # it is, we have to perform a different operation than if
                    # it isn't.

                    if current_node is self.tail:

                        # The Node we want to delete has been found, and it
                        # turns out to be the list's tail. Deleting a
                        # DoublyLinkedList's tail is similar to deleting it's
                        # head. First, we reassign the tail to become the Node
                        # at it's prev_node pointer. Then, we assign the new
                        # tail's next_node pointer to be None. Both of these
                        # steps happen below, on lines 177 and 178.

                        self.tail = current_node.prev_node
                        self.tail.next_node = None

                    else:

                        # If the Node we want to delete has been found and it
                        # isn't the DoublyLinkedList's tail Node, we delete the
                        # Node by ensuring no other Nodes point to it. This is
                        # accomplished below on lines 195 and 205.

                        # Since current_node is the Node we want to delete, we
                        # need to make sure it's next_node (the Node after it
                        # in the list) and prev_node (the Node before it in the
                        # list) no longer point to it. Once that process is
                        # complete, current_node becomes garbage collected
                        # (deleted) because it is no longer being referenced in
                        # memory.

                        current_node.prev_node.next_node = current_node.next_node

                        # First, on line 195 above, we target current_node's
                        # prev_node. We reassign that Node's next_node pointer
                        # to equal current_node's next_node. By doing this, we
                        # ensure that current_node's prev_node is not only no
                        # longer pointing to current_node but that it's
                        # correctly pointing to current_node's next_node, which
                        # preserves the integrity of our DoublyLinkedList.

                        current_node.next_node.prev_node = current_node.prev_node

                        # Next, on line 205 above, we target current_node's
                        # next_node. We reassign that Node's prev_node pointer
                        # to equal current_node's prev_node. By doing this we
                        # have again ensured that current_node's next_node is
                        # no longer pointing to it and that it's pointer is
                        # correctly assigned to current_node's prev_node.

                    # Now that current_node's next_node and prev_node pointers
                    # are no longer pointing to current_node, it will be
                    # deleted. Success! Since our job is done we simply return
                    # a string that both indicates a successful operation to
                    # the user and ceases execution of our method.

                    return 'Node has been deleted.'

                # If we've hit this point in the execution of our while loop,
                # it means we haven't yet landed on the Node we wish to delete.
                # So we reassign current_node to be it's next_node and then
                # continue iterating. We perform this reassignment below on
                # line 228.

                current_node = current_node.next_node

        # If either the list has no head Node (meaning that it's empty) or a
        # Node with the given data is not found in the list, we raise a
        # LookupError. Although not necessary, it indicates that the operation
        # was not performed so that the user is aware.

        raise LookupError("""No Node containing given value exists in Doubly
                          Linked List.""")

    def append(self, data):
        """Method to add new Node at tail of DoublyLinkedList."""

        # OVERVIEW
        # Appending a Node to a DoublyLinkedList is just like adding a Node
        # using the add_node method, except we're adding the new Node to the
        # end of our list instead of at the beginning. This process is simple
        # due to the list's tail. We'll create a variable that represents the
        # old tail of our list, reassign the tail to become a new Node with the
        # given data, and then based upon if our list is empty or not we'll
        # reassign other pointers accordingly. Easy!

        # On line 255 below we create a new variable called old_tail that
        # will represent our list's soon-to-be old tail. Next, on line 256, we
        # reassign the tail to be a new Node with a prev_node pointer that
        # points to our old_tail variable.

        old_tail = self.tail
        self.tail = Node(data, None, old_tail)

        # At this point we've already done most of the work. The newly appended
        # Node is now the list's new tail, as it should be, and the only thing
        # left for us to do is ensure that the list's old tail has a next_node
        # pointer that points at the new tail. However, if the list we just
        # appended to was previously empty, our old_tail variable will be None,
        # and trying to use old_tail.next_node will raise an exception.
        # Furthermore, we need to ensure that the list's head is correctly
        # assigned if the list was previously empty. So, on line 268 below, we
        # perform a simple check to see if the list was previously empty.

        if self.head:

            # If the list wasn't empty, all we have to do is assign the
            # old_tail's next_node pointer to be the new tail. It's that
            # simple!

            old_tail.next_node = self.tail

        else:

            # If the list was empty, we just have to ensure that it's head is
            # correctly assigned to be it's tail. Easy, right?

            self.head = self.tail

    def shift(self):
        """Method to remove and return value of tail in DoublyLinkedList."""

        # OVERVIEW
        # This method will perform and behave almost exactly like the pop
        # method (on both our DoublyLinkedList and our SinglyLinkedList), the
        # only difference being that instead of operating on the list's head
        # Node it instead operates on the list's tail Node.

        # The first step is to ensure the list isn't empty. If it is, we can't
        # remove and return the list's tail Node data because it isn't there.
        # We perform this check on line 298 below. Note that we could have also
        # checked for the list's head, as we've done in the past, but checking
        # for the tail is another way of ensuring the list isn't empty.

        if self.tail:

            # If the list contains at least one Node, we land here. We'll
            # define a variable that contains the current tail's data. That way
            # we can return the old tail's data after we reassign the list's
            # tail. That variable, called old_tail_data, is defined below.

            old_tail_data = self.tail.data

            if self.tail.prev_node:

                self.tail = self.tail.prev_node
                self.tail.next_node = None

            else:

                self.tail = None
                self.head = None

            return old_tail_data

        raise IndexError("""Cannot perform shift on an empty list.""")
