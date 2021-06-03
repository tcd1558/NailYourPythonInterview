class Stack():

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack == []

# TDD
# A stack can be created
def setup_function():
    my_stack = Stack()
    print(my_stack.stack)
    return my_stack

# Method: push
# Something can be added to the stack
def test_pushOnStack():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.stack)

# More can be added to the stack
def test_pushMoreOnStack():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    my_stack.push('carrot')
    print(my_stack.stack)

# Method: pop
# Something can be removed from the stack
def test_popStack():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.pop())
    print(my_stack.stack)

# Nothing happens, when something is removed from an empty stack
def test_popEmptyStack():
    my_stack = Stack()
    print(my_stack.stack)
    print(my_stack.pop())
    print(my_stack.stack)

# Method: peek
# The last element from the stack is displayed
# Nothing happens if the last element of an empty stack is displayed
def test_peekStack():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.peek())
    my_stack.push('banana')
    print(my_stack.peek())
    my_stack.push('carrot')
    print(my_stack.peek())
    print(my_stack.pop())  # carrot
    print(my_stack.peek())
    print(my_stack.pop())  # banana
    print(my_stack.peek())
    print(my_stack.pop())  # apple
    print(my_stack.peek())
    print(my_stack.pop())  # empty
    print(my_stack.peek())
    print(my_stack.pop())  # empty
    print(my_stack.stack)
    pass

# Method: size
# After creating the stack, the stack size is 0
def test_StackSize():
    my_stack = Stack()
    print(my_stack.stack, my_stack.size())
    assert my_stack.size() == 0

# After adding one item to the stack, the stack size is 1
def test_StackSizeOne():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.stack, my_stack.size())
    assert my_stack.size() == 1

# After adding another item to the stack, the stack size is 2
def test_StackSizeTwo():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    print(my_stack.stack, my_stack.size())
    assert my_stack.size() == 2

# After peeking the stack, the stack size is still the same
def test_StackSizeTwoPeek():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    print(my_stack.stack, my_stack.size(), my_stack.peek())
    assert my_stack.size() == 2

# After popping the stack, the stack size is reduced by 1
def test_StackSizeTwoPop():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    print(my_stack.stack, my_stack.size(), my_stack.pop())
    assert my_stack.size() == 1

# After popping the stack emply, the stack size is 0.
def test_StackSizeTwoPopPop():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    my_stack.pop()
    print(my_stack.stack, my_stack.size(), my_stack.pop())
    assert my_stack.size() == 0

# Method: is_empty
# Calling is_empty on a just created stack is True
def test_StackIs_empty():
    my_stack = Stack()
    print(my_stack.stack)
    assert my_stack.size() == 0
    assert my_stack.is_empty() == True

# Calling is_empty on a pushed stack is False
def test_StackPushIs_empty():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.stack)
    assert my_stack.size() == 1
    return my_stack.is_empty() == False

# Calling is_empty on a stack being popped empty is True
def test_StackPushPopIs_empty():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.stack, my_stack.pop())
    assert my_stack.size() == 0
    return my_stack.is_empty() == False