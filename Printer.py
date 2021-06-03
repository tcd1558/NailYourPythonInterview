import pytest

class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list. Returns nothing

        :runtime: The runtime for this method is O(n), because inserting
        to the beginning of a list requires shifting the rest of the list by 1.

        :note: It would be good to investigate on how a list is implemented in python.
        Is there a performance impact in the way how a queue is implemented:
        front of queue is end of list or front of queue is beginning of the list.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
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
        Return the length of the stack
        :return:
        :runtime: The runtime for this method is O(1), or constatnt time.
        """
        return len(self.items)

    def isEmpty(self):
        """
        Return a Boolean value.
        :return:
        True: the stack is empty
        False: there is an item in the stack

        :Runtime:
        Since this calls a methon with O(1), this is also O(1), or constant time.
        """
        # return self.size() == 0
        return self.items == []










# A stack can be created
#def setup_function():
#    my_queue = Queue()
#    print(my_queue.items)
#    return my_queue

# Method: enqueue
# Something can be added to the Queue
@pytest.mark.skip
def test_enqueueOnQueue():
    my_queue = Queue()
    my_queue.enqueue('apple')
    print(my_queue.items)

# More can be added to the Queue
@pytest.mark.skip
def test_enqueueMoreOnQueue():
    my_queue = Queue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    my_queue.enqueue('carrot')
    print(my_queue.items)

# Method: dequeue
# Something can be removed from the Queue
@pytest.mark.skip
def test_dequeueQueue():
    my_queue = Queue()
    my_queue.enqueue('apple')
    print(my_queue.dequeue())
    print(my_queue.items)

# Nothing happens, when something is removed from an empty Queue
@pytest.mark.skip
def test_dequeueEmptyQueue():
    my_queue = Queue()
    print(my_queue.items)
    print(my_queue.dequeue())
    print(my_queue.items)

# Method: peek
# The last element from the Queue is displayed
# Nothing happens if the last element of an empty Queue is displayed
@pytest.mark.skip
def test_peekQueue():
    my_queue = Queue()
    my_queue.enqueue('apple')
    print(my_queue.peek())
    my_queue.enqueue('banana')
    print(my_queue.peek())
    my_queue.enqueue('carrot')
    print(my_queue.peek())
    print(my_queue.dequeue()) # carrot
    print(my_queue.peek())
    print(my_queue.dequeue()) # banana
    print(my_queue.peek())
    print(my_queue.dequeue()) # apple
    print(my_queue.peek())
    print(my_queue.dequeue()) # empty
    print(my_queue.peek())
    print(my_queue.dequeue()) # empty
    print(my_queue.items)
    pass


# Method: size
# After creating the Queue, the Queue size is 0
@pytest.mark.skip
def test_QueueSize():
    my_queue = Queue()
    print(my_queue.items, my_queue.size())
    assert my_queue.size() == 0

# After adding one item to the Queue, the Queue size is 1
@pytest.mark.skip
def test_QueueSizeOne():
    my_queue = Queue()
    my_queue.enqueue('apple')
    print(my_queue.items, my_queue.size())
    assert my_queue.size() == 1

# After adding another item to the Queue, the Queue size is 2
@pytest.mark.skip
def test_QueueSizeTwo():
    my_queue = Queue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    print(my_queue.items, my_queue.size())
    assert my_queue.size() == 2


# After peeking the Queue, the Queue size is still the same
@pytest.mark.skip
def test_QueueSizeTwoPeek():
    my_queue = Queue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    print(my_queue.items, my_queue.size(), my_queue.peek())
    assert my_queue.size() == 2

# After dequeueping the Queue, the Queue size is reduced by 1
@pytest.mark.skip
def test_QueueSizeTwodequeue():
    my_queue = Queue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    print(my_queue.items, my_queue.size(), my_queue.dequeue())
    assert my_queue.size() == 1

# After dequeueping the Queue emply, the Queue size is 0.
@pytest.mark.skip
def test_QueueSizeTwodequeuedequeue():
    my_queue = Queue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    my_queue.dequeue()
    print(my_queue.items, my_queue.size(), my_queue.dequeue())
    assert my_queue.size() == 0

# Method: isEmpty
# Calling isEmpty on a just created Queue is True
@pytest.mark.skip
def test_QueueIsEmpty():
    my_queue = Queue()
    print(my_queue.items)
    assert my_queue.size() == 0
    assert my_queue.isEmpty() == True

# Calling isEmpty on a enqueueed Queue is False
@pytest.mark.skip
def test_QueueenqueueIsEmpty():
    my_queue = Queue()
    my_queue.enqueue('apple')
    print(my_queue.items)
    assert my_queue.size() == 1
    return my_queue.isEmpty() == False

# Calling isEmpty on a Queue being dequeueped empty is True
@pytest.mark.skip
def test_QueueenqueuedequeueIsEmpty():
    my_queue = Queue()
    my_queue.enqueue('apple')
    print(my_queue.items, my_queue.dequeue())
    assert my_queue.size() == 0
    return my_queue.isEmpty() == False

# TDD

# 3 Classes:
# PrintQueue = Queue()
# Job - Class with pages attribute. pages are assigned randomly (1 to 10)
#   Job Class has a PrintJob (page wise) (was print_page) method, which sends a job to the Printer (calls Printer.print_job(Job))
#   Job Class has a CheckComplete method, which checks all pages have been printed
#       meaning pages == 0
# class Printer - GetJob() method. Check whether a Job is not completed already.
#   use PrintQueue.dequeue() method to take first job of queue
#   Check (PrintQueue.isEmpty() == False) resp (PrintQueue.items == [])
#   print_job() - prints a page, sleeps 1s.

# The PrintQueue holds Jobs
# The Printer removes Jobs from the PrintQueue
# The Job class adds pages to the Printer using the method PrintPage

from random import randint
from time import sleep


class Job():

    def __init__(self):
        self.pages = randint(0,11)

    def PrintPage(self):
        self.pages -= 1
        return

    def CheckComplete(self):
        if self.pages == 0:
            return True
        else:
            return False

class Printer():

    def __init__(self):
        self.no_active_job = True

    def GetJob(self):
        """
        Checks, if a job needs to be retreived from the printQueue

        :return:
        True, if there is no active job
        False, if there is an active job
        """

        return self.no_active_job

    def print_job(self, job):
        if self.no_active_job:
            self.no_active_job = False
            while not self.no_active_job:
                if job.CheckComplete():
                    self.no_active_job = True
                    print('Done printing')
                    print()
                else:
                    job.PrintPage()
                    # sleep(2)
                    print('Pages to print', job.pages)
            return
        else:
            return "printing .."


#@pytest.fixture()
#def printQueue():
#    printQueue = Queue()
#    return printQueue

#def setup_function():
#    printQueue = Queue()
#    return printQueue

def test_PrinterQueueExists():
    printQueue = Queue()

def test_AddJobClass():
    printQueue = Queue()
    new_job = Job()
    printQueue.enqueue(new_job)
    print(printQueue.items)

def test_Printer():
    printQueue = Queue()
    myPrinter = Printer()
    # Create a new job
    new_job1 = Job()
    new_job2 = Job()
    new_job3 = Job()
    new_job4 = Job()
    # Add a job to the queue
    printQueue.enqueue(new_job1)
    printQueue.enqueue(new_job2)
    printQueue.enqueue(new_job3)
    printQueue.enqueue(new_job4)
    print("printQueue.items: ", printQueue.items)
    print('myPrinter.GetJob():', myPrinter.GetJob())
    if (myPrinter.GetJob()):
        print("There is no active job")
        print(printQueue.isEmpty())
        while not printQueue.isEmpty():
            print("dequeue a job from the Queue")
            jobToPrint = printQueue.dequeue()
            print('printing: ', jobToPrint)
            myPrinter.print_job(jobToPrint)
        print('the printQueue is empty')
    else:
        print('there is an active job')
    return



