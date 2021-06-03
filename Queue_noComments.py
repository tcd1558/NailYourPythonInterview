class Queue():

    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.insert(0,item)

    def pop(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == []


def setup_function():
    my_queue = Queue()
    print(my_queue.queue)
    return my_queue

    # Method: insert
    # Something can be added to the Queue


def test_insertOnQueue():
    my_queue = Queue()
    my_queue.insert('apple')
    print(my_queue.queue)

    # More can be added to the Queue


def test_insertMoreOnQueue():
    my_queue = Queue()
    my_queue.insert('apple')
    my_queue.insert('banana')
    my_queue.insert('carrot')
    print(my_queue.queue)

    # Method: pop
    # Something can be removed from the Queue


def test_popQueue():
    my_queue = Queue()
    my_queue.insert('apple')
    print(my_queue.pop())
    print(my_queue.queue)

    # Nothing happens, when something is removed from an empty Queue


def test_popEmptyQueue():
    my_queue = Queue()
    print(my_queue.queue)
    print(my_queue.pop())
    print(my_queue.queue)

    # Method: peek
    # The last element from the Queue is displayed
    # Nothing happens if the last element of an empty Queue is displayed


def test_peekQueue():
    my_queue = Queue()
    my_queue.insert('apple')
    print(my_queue.peek())
    my_queue.insert('banana')
    print(my_queue.peek())
    my_queue.insert('carrot')
    print(my_queue.peek())
    print(my_queue.pop())  # carrot
    print(my_queue.peek())
    print(my_queue.pop())  # banana
    print(my_queue.peek())
    print(my_queue.pop())  # apple
    print(my_queue.peek())
    print(my_queue.pop())  # empty
    print(my_queue.peek())
    print(my_queue.pop())  # empty
    print(my_queue.queue)
    pass

    # Method: size
    # After creating the Queue, the Queue size is 0


def test_QueueSize():
    my_queue = Queue()
    print(my_queue.queue, my_queue.size())
    assert my_queue.size() == 0

    # After adding one item to the Queue, the Queue size is 1


def test_QueueSizeOne():
    my_queue = Queue()
    my_queue.insert('apple')
    print(my_queue.queue, my_queue.size())
    assert my_queue.size() == 1

    # After adding another item to the Queue, the Queue size is 2


def test_QueueSizeTwo():
    my_queue = Queue()
    my_queue.insert('apple')
    my_queue.insert('banana')
    print(my_queue.queue, my_queue.size())
    assert my_queue.size() == 2

    # After peeking the Queue, the Queue size is still the same


def test_QueueSizeTwoPeek():
    my_queue = Queue()
    my_queue.insert('apple')
    my_queue.insert('banana')
    print(my_queue.queue, my_queue.size(), my_queue.peek())
    assert my_queue.size() == 2

    # After popping the Queue, the Queue size is reduced by 1


def test_QueueSizeTwoPop():
    my_queue = Queue()
    my_queue.insert('apple')
    my_queue.insert('banana')
    print(my_queue.queue, my_queue.size(), my_queue.pop())
    assert my_queue.size() == 1

    # After popping the Queue emply, the Queue size is 0.


def test_QueueSizeTwoPopPop():
    my_queue = Queue()
    my_queue.insert('apple')
    my_queue.insert('banana')
    my_queue.pop()
    print(my_queue.queue, my_queue.size(), my_queue.pop())
    assert my_queue.size() == 0

    # Method: is_empty
    # Calling is_empty on a just created Queue is True


def test_Queueis_empty():
    my_queue = Queue()
    print(my_queue.queue)
    assert my_queue.size() == 0
    assert my_queue.is_empty() == True

    # Calling is_empty on a inserted Queue is False


def test_Queueinsertis_empty():
    my_queue = Queue()
    my_queue.insert('apple')
    print(my_queue.queue)
    assert my_queue.size() == 1
    return my_queue.is_empty() == False

    # Calling is_empty on a Queue being popped empty is True


def test_QueueinsertPopis_empty():
    my_queue = Queue()
    my_queue.insert('apple')
    print(my_queue.queue, my_queue.pop())
    assert my_queue.size() == 0
    return my_queue.is_empty() == False