import pytest

class Queue():

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        1
        Accepts an item as a parameter and appends it to the end of the list. Returns nothing

        :runtime: The runtime for this method is O(n), because inserting
        to the beginning of a list requires shifting the rest of the list by 1.

        :note: It would be good to investigate on how a list is implemented in python.
        Is there a performance impact in the way how a queue is implemented:
        front of queue is end of list or front of queue is beginning of the list.
        """
        self.items.insert(0, item)

    def pop(self):
        """
        2
        Remove an item from the top of the stack.
        :return:
        The last value of the list. This item has them been removed from the list.

        :runtime: The runtime for this method is O(1), or constant time. A list item is accessed through its index.
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        3
        Show the last item on the stack/in the list. The stack remains unchanged.
        :return:
        :runtime: The runtime for this method is O(1), or constant time. A list item is accessed through its index.
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """
        4
        Return the length of the stack
        :return:
        :runtime: The runtime for this method is O(1), or constatnt time.
        """
        return len(self.items)

    def isEmpty(self):
        """
        5
        Return a Boolean value.
        :return:
        True: the stack is empty
        False: there is an item in the stack

        :Runtime:
        Since this calls a methon with O(1), this is also O(1), or constant time.
        """
        # return self.size() == 0
        return self.items == []

# TDD
# A stack can be created
def setup_function():
    my_queue = Queue()
    print(my_queue.items)
    return my_queue

# Method: push
# Something can be added to the Queue
def test_pushOnQueue():
    my_queue = Queue()
    my_queue.push('apple')
    print(my_queue.items)

# More can be added to the Queue
def test_pushMoreOnQueue():
    my_queue = Queue()
    my_queue.push('apple')
    my_queue.push('banana')
    my_queue.push('carrot')
    print(my_queue.items)

# Method: pop
# Something can be removed from the Queue
def test_popQueue():
    my_queue = Queue()
    my_queue.push('apple')
    print(my_queue.pop())
    print(my_queue.items)

# Nothing happens, when something is removed from an empty Queue
def test_popEmptyQueue():
    my_queue = Queue()
    print(my_queue.items)
    print(my_queue.pop())
    print(my_queue.items)

# Method: peek
# The last element from the Queue is displayed
# Nothing happens if the last element of an empty Queue is displayed
def test_peekQueue():
    my_queue = Queue()
    my_queue.push('apple')
    print(my_queue.peek())
    my_queue.push('banana')
    print(my_queue.peek())
    my_queue.push('carrot')
    print(my_queue.peek())
    print(my_queue.pop()) # carrot
    print(my_queue.peek())
    print(my_queue.pop()) # banana
    print(my_queue.peek())
    print(my_queue.pop()) # apple
    print(my_queue.peek())
    print(my_queue.pop()) # empty
    print(my_queue.peek())
    print(my_queue.pop()) # empty
    print(my_queue.items)
    pass


# Method: size
# After creating the Queue, the Queue size is 0
def test_QueueSize():
    my_queue = Queue()
    print(my_queue.items, my_queue.size())
    assert my_queue.size() == 0

# After adding one item to the Queue, the Queue size is 1
def test_QueueSizeOne():
    my_queue = Queue()
    my_queue.push('apple')
    print(my_queue.items, my_queue.size())
    assert my_queue.size() == 1

# After adding another item to the Queue, the Queue size is 2
def test_QueueSizeTwo():
    my_queue = Queue()
    my_queue.push('apple')
    my_queue.push('banana')
    print(my_queue.items, my_queue.size())
    assert my_queue.size() == 2


# After peeking the Queue, the Queue size is still the same
def test_QueueSizeTwoPeek():
    my_queue = Queue()
    my_queue.push('apple')
    my_queue.push('banana')
    print(my_queue.items, my_queue.size(), my_queue.peek())
    assert my_queue.size() == 2

# After popping the Queue, the Queue size is reduced by 1
def test_QueueSizeTwoPop():
    my_queue = Queue()
    my_queue.push('apple')
    my_queue.push('banana')
    print(my_queue.items, my_queue.size(), my_queue.pop())
    assert my_queue.size() == 1

# After popping the Queue emply, the Queue size is 0.
def test_QueueSizeTwoPopPop():
    my_queue = Queue()
    my_queue.push('apple')
    my_queue.push('banana')
    my_queue.pop()
    print(my_queue.items, my_queue.size(), my_queue.pop())
    assert my_queue.size() == 0

# Method: isEmpty
# Calling isEmpty on a just created Queue is True
def test_QueueIsEmpty():
    my_queue = Queue()
    print(my_queue.items)
    assert my_queue.size() == 0
    assert my_queue.isEmpty() == True

# Calling isEmpty on a pushed Queue is False
def test_QueuePushIsEmpty():
    my_queue = Queue()
    my_queue.push('apple')
    print(my_queue.items)
    assert my_queue.size() == 1
    return my_queue.isEmpty() == False

# Calling isEmpty on a Queue being popped empty is True
def test_QueuePushPopIsEmpty():
    my_queue = Queue()
    my_queue.push('apple')
    print(my_queue.items, my_queue.pop())
    assert my_queue.size() == 0
    return my_queue.isEmpty() == False