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
        return "Single Link List object: data={}".format(self.data)

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
    Own implementation:

    Create a list
    Save a pointer to the first and last element
    When a new node is created, the next pointer defaults to None

    None; first -> None, last -> None
    |a| -> None ; first -> |a|, last -> |a|
    |a| -> |b| -> None; first -> |a|, last -> |b|
    |a| -> |b| -> |c| -> None, first -> |a| , last -> |c|


    """

    def __init__(self):
        self.single_linked_list = []    # Do not use another list. The objects are
                                        # connected together via the next attribute
        self.last_node = None
        self.first_node = None  # head
 
    def __repr__(self):
        return "SLL object: head={}".format(self.first_node)

    def is_empty(self):
        return self.first_node is None

    def add_front(self, item):
        """
        Append/Add something to the single linked list.
        :param item:
        :return:
        """
        self.single_linked_list.append(item)
        if self.size() > 1 :
            # if this is not the first node added to the list
            self.last_node.next = self.single_linked_list[-1]
        else:
            # if this is the first noded added to the list
            self.first_node = self.single_linked_list[0]
        self.last_node = self.single_linked_list[-1]

    def insert_before(self, pattern, item):
        # This included the first_node/head, which
        # requires to replace self.first_node
        pass

    def insert_before_first_node(self, item):
        self.insert_before(self, self.first_node.data, item)
        pass

    def size(self):
        return len(self.single_linked_list)

    def search(self,data):
        if self.first_node.data == data:
            print_snode(self.first_node)
            return self.first_node
        else:
            next = self.first_node.next
            while next.data != data:
                next = next.next
            else:
                print_snode(next)
                return next

    def remove(self, data):
        # find node
        # change previous_node.next to current_node.next
        if self.first_node.data == data:
            print_snode(self.first_node)
            self.first_node = self.first_node.next
            # remove from self.single_linked_list
        else:
            next = self.first_node.next
            while next.data != data:
                prev = next
                next = next.next
            else:
                prev.next = next.next
                # remove from self.single_linked_list


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
    my_single_linked_list = SingleLinkedList()
    print(my_single_linked_list.is_empty())

    # Create a single_linked_list_Node and add it to the single_linked_list
    mySNode1 = SingleLinkedList_Node('apple')
    my_single_linked_list.add_front(mySNode1)
    print(my_single_linked_list.is_empty())
    print(my_single_linked_list.single_linked_list)
    print(my_single_linked_list.size())

    # Create another single_linked_list_Node and add it to the single_linked_list
    mySNode2 = SingleLinkedList_Node('banana')
    my_single_linked_list.add_front(mySNode2)
    mySNode3 = SingleLinkedList_Node('carrot')
    my_single_linked_list.add_front(mySNode3)
    print('is_empty:', my_single_linked_list.is_empty())
    print('single_linked_list:', my_single_linked_list.single_linked_list)
    print('Size:', my_single_linked_list.size())
    for node in my_single_linked_list.single_linked_list:
        print_snode(node)
    print()
    print("Search:")
    my_single_linked_list.search('carrot')
    my_single_linked_list.search('banana')
    my_single_linked_list.search('apple')

    print()
    print("Remove:")
    my_single_linked_list.remove('apple')
    for node in my_single_linked_list.single_linked_list:
        print_snode(node)
