class SingleLinkedList_Node():
    """
    An Object oriented class of a single linked list node
    """

    def __init__(self, data):
        """
        A list with 'data' and a pointer to the next node.
        If there is no next node, the pointer points to None

        :param data:

        <var> = a class attribute
        self.<var> = an instance attribute
        """
        self.data = data
        self.next = None

    def __repr__(self):
        return "Single Link List object: data={}, next={}".format(self.data, self.get_next())

    def get_data(self):
        """
        :return:
        Return the self.data instance attribute
        """
        return self.data

    def set_data(self, new_data):
        """
        Replace the self.data instance attribute with new_data parameter

        :param new_data:
        new_data is the value you want to store for this node

        """
        self.data = new_data

    def get_next(self):
        """
        :return:
        Return the self.next instance attribute.
        """
        return self.next

    def set_next(self, new_next):
        """
        :param new_next:
        Set the self.next instant attribute to new_next

        :return:
        """
        self.next = new_next


class DoubleLinkedList_Node():
    """
    An Object Oriented implementation of double linked list node
    """

    # Dunder Names
    def __init__(self, data):
        """
        A list with 'data' and a pointer to the next node.
        If there is no next node, the pointer points to None

        :param data:

        <var> = a class attribute
        self.<var> = an instance attribute
        """
        self.data = data
        self.next = None # last node points to None
        self.prev = None # first node points to None

    def __repr__(self):
        """
        Representation. When this object is printed, it uses the value being returned by the __repr__ method
        """
        return "Double Link List object: data={}".format(self.data)
        # when accessing self.prev, it tries to execute __repr__ of self.prev:
        # return "Double Link List object: data={}, prev={}, next={}".format(self.data, self.prev, self.next)

    #def __all__(self):
    #def __author__(self):
    #def __version__(self):

    # imports go here

    def get_data(self):
        """
        :return:
        Return the self.data instance attribute
        """
        return self.data

    def set_data(self, new_data):
        """
        Replace the self.data instance attribute with new_data parameter

        :param new_data:
        new_data is the value you want to store for this node

        """
        self.data = new_data

    def get_next(self):
        """
        :return:
        Return the self.next instance attribute.
        """
        return self.next

    def set_next(self, new_next):
        """
        :param new_next:
         Set the self.next instant attribute to new_next

        :return:
        """
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev


class SingleLinkedList():

    """
    To access the SLL, the class includes a pointer to self.head, a pointer to the first element.

    """

    def __init__(self):
        self.head = None  # head is the first node. It is the entry into the SLL

    def __repr__(self):
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        """
        1
        A SLL is empty if the entry pointer points to None.
        :return:
        True, if the pointer is None.
        False, if the pointer points to an element of the SLL.
        """
        return self.head is None

    def add_front(self, data):
        """
        2
        As long as Python is running, objects created in the program exist.
        When Python is terminated, objects should be cleaned up.

        self.head = None
        self.head = |a| -> None
        self.head = |b| -> |a| -> None
        self.head = |c| -> |b| -> |a| -> None

        :param data:
        data to add to the SSL_Node

        :return:
        """
        temp = SingleLinkedList_Node(data)
        temp.set_next(self.head)
        self.head = temp

    def insert_before(self, pattern, data):
        # This included the first_node/head, which
        # requires to replace self.first_node
        pass

    def insert_before_first_node(self, data):
        self.insert_before(self, self.first_node.data, item)
        pass

    def size(self):
        """
        3
        :return:
        :complexity:
        O(n). The entire linked list has to be traversed to count the size.
        """
        size = 0
        current = self.head
        while current is not None:
            print(current)
            size += 1
            print("new size:", size)
            current = current.get_next()
        return size

    def search(self, data):
        """
        4
        Traverse the Linked List.
        Returns a pointer to the node containing data
        Only the first result is returned.

        If the data is not found, None is returned.

        :param data:
        :return:
        : complexity:
        O(n)
        """
        current = self.head
        result = None
        while current is not None:
            # print(current.get_data(), '-', data )
            if current.get_data() is data:
                result = current
                current = None # to break the loop. Assuming data is unique
                # better:
                # return current
            else:
                current = current.get_next()
        # Result is set to None by default
        # If there is no matching data, None is returned
        # If a result was found, result is returned.
        return result

    def remove(self, data):
        """
        5
        self.head = None
        self.head = |a| -> None
        self.head = |b| -> |a| -> None
        self.head = |c| -> |b| -> |a| -> None

        No Element:
        it self.head = None - there is nothing to remove.
        return False

        Only Element:
        if self.head = |a| and next points to None,
            |a| was what was looked for,
            self.head has to be set to None
        return True

        Last Element:
        if self.head = |b| and we look for |a|,
            you have to find |a| first (would be nice to use the search method),
            if |a|->None, you have to set |b|->None
        return True

        First Element of 2 or more:
        Middle Element:


        return:
        True - object was remove
        Fals - object was not found
        """

        if self.head is None:
            return False
        else:
            current = self.head
            previous = None
            result = None
            while current is not None:
                # print(current.get_data(), '-', data )
                if current.get_data() is data:
                    # Delete the node:
                    #   Change previous.next to current.next (could be None)
                    #   if previous is None, set self.head to current.next

                    result = current
                    if previous is None:
                        # It is the first element.
                        # delete it by setting the head pointer to next
                        self.head = current.get_next()
                        return True
                    else:
                        # it is not the first
                        previous.set_next(current.get_next())
                        return True
                    current = None # to break the loop
                else:
                    # move to the next node
                    previous = current
                    current = current.get_next()

            # Result is set to None by default
            # If there is no matching data, False is returned
            # If a result was found, result is returned.
            return False


class DoubleLinkedList():

    """
    A double linked list can be accessed through a head pointer. All other activity can be accessed
    through following this head pointer
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "DLL object: head={}, prev={}, next={}".format(self.head, self.head.get_prev(), self.head.get_next())

    def is_empty(self):
        """
        1
        :return:
        """
        #if self.head is None:
        #    return True
        #else:
        #    return False
        return self.head is None

    def add_front(self, data):
        """
        2
        A double linked list node includes 3 values:
            pointer to previous
            data
            pointer to nex

        None, self.head = None
        None<-|a|->Node, self.head->a
        None<-|b|->a, b<-|a|->None, self.head->b
        None<-|c|->b, c<-|b|->a, b<-|a|->None, self.head->c

        If you would create a circular structure, by having the last element pointing
        to the first, you will not know, when you have completed a traverse.

        Create a new DLL node tmp
        If a node is added to an empty list, self.head has to point to the new node.
            self.head = tmp

        :param data:
        :return:
        """
        tmp = DoubleLinkedList_Node(data)
        current=self.head
        if current is None:
            # There is no element
            print("Current is None")
            self.head = tmp
            self.tail = tmp
            tmp.next = None
            tmp.prev = None
        else:
            if current.prev is None:
                # There is one or more elements
                # first element
                # This is the default, because add_front should insert in the first possition
                # There is no difference with one or N elements.
                current.prev = tmp
                tmp.next = current
                tmp.prev = None # = current.prev
                self.head = tmp
            else:
                # do nothing, because add_front insert in the first possition.
                True

    def size(self):
        """
        3
        :return:
        """
        size = 0
        current = self.head
        while current is not None:
            print(current)
            size += 1
            print("new size:", size)
            current = current.get_next()
        return size

    def reverse_size(self):
        size = 0
        current = self.tail
        while current is not None:
            print(current)
            size += 1
            print("new size:", size)
            current = current.get_prev()
        return size

    def search(self,data):
        """
        4
        :param item:
        :return:
        """
        current = self.head
        result = None
        while current is not None:
            if current.data is data:
                return current
            else:
                current = current.get_next()
        return None

    def reverse_search(self, data):
        """
        A search starting from the end
        :param item:
        :return:
        """
        current = self.tail
        result = None
        while current is not None:
            if current.data is data:
                return current
            else:
                current = current.get_prev()
        return None

    def remove(self, data):
        """
        5

        :param item:
        :return:
        """

        if self.head is None:
            return False
        else:
            current = self.head
            result = None
            while current is not None:
                # print(current.get_data(), '-', data )
                if current.get_data() is data:
                    # Delete the node:
                    #   Change previous.next to current.next (could be None)
                    #   if previous is None, set self.head to current.next

                    result = current
                    if current.prev is None:
                        # It is the first element.
                        # delete it by setting the head pointer to next
                        self.head = current.get_next()
                        self.head.prev = None
                        return True
                    else:
                        # it is not the first
                        previous = current.get_prev()
                        print(previous)
                        previous.set_next(current.get_next())
                        my_next = current.get_next()
                        print(my_next)
                        my_next.set_prev(current.get_prev())
                        return True
                    current = None # to break the loop
                else:
                    # move to the next node
                    previous = current
                    current = current.get_next()

            # Result is set to None by default
            # If there is no matching data, False is returned
            # If a result was found, result is returned.
            return False

# Test Single Linked List

def print_snode(node):
    print('--', 'node: ', node.get_data(), '--', 'next: ', node.get_next())

def test_SingleLinkedList_Node():
    myNode = SingleLinkedList_Node('apple')
    print_snode(myNode)
    myNode.set_data('banana')
    print_snode(myNode)

    print()

    myNode2 = SingleLinkedList_Node('carrot')
    myNode.set_next(myNode2)
    print_snode(myNode)
    print_snode(myNode2)
    print(myNode.next.get_data())


# Test double linked list

def print_dnode(node):
    print('--', 'node: ', node.get_data(), '--', 'next: ', node.get_next(), '--', 'prev: ', node.get_prev())

def test_DoubleLinkedList_Node():
    myDNode = DoubleLinkedList_Node('carrot')
    print_dnode(myDNode)
    myDNode.set_data('banana')
    print_dnode(myDNode)

    print()

    myDNode2 = DoubleLinkedList_Node('carrot')
    myDNode.set_next(myDNode2)
    myDNode2.set_prev(myDNode)
    print_dnode(myDNode)
    print_dnode(myDNode2)
    print(myDNode.next.get_data())

    myDNode3 = DoubleLinkedList_Node('date')
    myDNode2.set_next(myDNode3)
    myDNode3.set_prev(myDNode2)
    print_dnode(myDNode)
    print_dnode(myDNode2)
    print_dnode(myDNode3)
    print(myDNode.next.get_data())
    print(myDNode2.next.get_data())


def test_SingleLinkedList():
    # Can I create a single_linked_list?
    print()
    print("Testing Single Linked List")
    my_single_linked_list = SingleLinkedList()
    print("Is the single linked list empty: ", my_single_linked_list.is_empty())

    # Create a single_linked_list_Node and add it to the single_linked_list
    print("Add node with 'apple' in front")
    my_single_linked_list.add_front('apple')
    print("Is the list empty: ", my_single_linked_list.is_empty())
    print("list head: ", my_single_linked_list.head)
    print("list size: ", my_single_linked_list.size())
    print()

    # Create another single_linked_list_Node and add it to the single_linked_list
    print("Add 2 more items to the list")
    my_single_linked_list.add_front('banana')
    my_single_linked_list.add_front('carrot')
    print('is_empty:', my_single_linked_list.is_empty())
    print('Size:', my_single_linked_list.size())

    print()
    print("Search:")
    print(my_single_linked_list.search('carrot'))
    print(my_single_linked_list.search('banana'))
    print(my_single_linked_list.search('apple'))

    print()
    print("Remove:")
    my_single_linked_list.remove('carrot')
    my_single_linked_list.remove('banana')
    my_single_linked_list.remove('apple')
    my_single_linked_list.remove('apple')

    print(my_single_linked_list.search('carrot'))
    print(my_single_linked_list.search('banana'))
    print(my_single_linked_list.search('apple'))

def test_DoubleLinkedList():
    print()
    print("Testing Double Linked List")
    my_double_linked_list = DoubleLinkedList()
    print("Is the double linked list empty: ", my_double_linked_list.is_empty())

    print()
    print("Add node with 'apple' in front")
    my_double_linked_list.add_front('apple')
    print(my_double_linked_list)
    print("Is the list empty: ", my_double_linked_list.is_empty())

    print()
    my_double_linked_list.add_front('banana')
    print(my_double_linked_list)

    print()
    my_double_linked_list.add_front('cherry')
    print("The list is represented by: ", my_double_linked_list)
    print("The next element: ", my_double_linked_list.head.get_next())
    my_next=my_double_linked_list.head.get_next()
    print("Of the next element, previous is pointing to: ", my_next.get_prev())
    print("Of the next element, next is pointing to: ",my_next.get_next())

    print()
    print("list size: ", my_double_linked_list.size())
    print("reverse list size: ", my_double_linked_list.reverse_size())

    print()
    print("Search")
    print("Search banana:")
    print(my_double_linked_list.search('banana'))
    print("Search apple:")
    print(my_double_linked_list.search('apple'))
    print("Search cherry:")
    print(my_double_linked_list.search('cherry'))
    print("Search berry:")
    print(my_double_linked_list.search('berry'))

    print()
    print("Reverse Search")
    print("Reverse Search banana:")
    print(my_double_linked_list.reverse_search('banana'))
    print("Reverse Search apple:")
    print(my_double_linked_list.reverse_search('apple'))
    print("Reverse Search cherry:")
    print(my_double_linked_list.reverse_search('cherry'))
    print("Reverse Search berry:")
    print(my_double_linked_list.reverse_search('berry'))

    print()
    print("Remove")
    print(my_double_linked_list.remove('banana'))
    print("The list is represented by: ", my_double_linked_list)
    print("The next element: ", my_double_linked_list.head.get_next())
    my_next = my_double_linked_list.head.get_next()
    print("Of the next element, previous is pointing to: ", my_next.get_prev())
    print("Of the next element, next is pointing to: ", my_next.get_next())
