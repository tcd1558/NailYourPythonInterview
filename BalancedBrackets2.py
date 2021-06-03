import pytest

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list. Returns nothing

        Runtime: The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
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
# TDD
# A stack can be created
def setup_function():
    my_stack = Stack()
    print(my_stack.items)
    return my_stack

# Method: push
# Something can be added to the stack
def test_pushOnStack():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.items)

# More can be added to the stack
def test_pushMoreOnStack():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    my_stack.push('carrot')
    print(my_stack.items)

# Method: pop
# Something can be removed from the stack
def test_popStack():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.pop())
    print(my_stack.items)

# Nothing happens, when something is removed from an empty stack
def test_popEmptyStack():
    my_stack = Stack()
    print(my_stack.items)
    print(my_stack.pop())
    print(my_stack.items)

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
    print(my_stack.pop()) # carrot
    print(my_stack.peek())
    print(my_stack.pop()) # banana
    print(my_stack.peek())
    print(my_stack.pop()) # apple
    print(my_stack.peek())
    print(my_stack.pop()) # empty
    print(my_stack.peek())
    print(my_stack.pop()) # empty
    print(my_stack.items)
    pass


# Method: size
# After creating the stack, the stack size is 0
def test_StackSize():
    my_stack = Stack()
    print(my_stack.items, my_stack.size())
    assert my_stack.size() == 0

# After adding one item to the stack, the stack size is 1
def test_StackSizeOne():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.items, my_stack.size())
    assert my_stack.size() == 1

# After adding another item to the stack, the stack size is 2
def test_StackSizeTwo():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    print(my_stack.items, my_stack.size())
    assert my_stack.size() == 2


# After peeking the stack, the stack size is still the same
def test_StackSizeTwoPeek():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    print(my_stack.items, my_stack.size(), my_stack.peek())
    assert my_stack.size() == 2

# After popping the stack, the stack size is reduced by 1
def test_StackSizeTwoPop():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    print(my_stack.items, my_stack.size(), my_stack.pop())
    assert my_stack.size() == 1

# After popping the stack emply, the stack size is 0.
def test_StackSizeTwoPopPop():
    my_stack = Stack()
    my_stack.push('apple')
    my_stack.push('banana')
    my_stack.pop()
    print(my_stack.items, my_stack.size(), my_stack.pop())
    assert my_stack.size() == 0

# Method: isEmpty
# Calling isEmpty on a just created stack is True
def test_StackIsEmpty():
    my_stack = Stack()
    print(my_stack.items)
    assert my_stack.size() == 0
    assert my_stack.isEmpty() == True

# Calling isEmpty on a pushed stack is False
def test_StackPushIsEmpty():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.items)
    assert my_stack.size() == 1
    return my_stack.isEmpty() == False

# Calling isEmpty on a stack being popped empty is True
def test_StackPushPopIsEmpty():
    my_stack = Stack()
    my_stack.push('apple')
    print(my_stack.items, my_stack.pop())
    assert my_stack.size() == 0
    return my_stack.isEmpty() == False

# StringBalance can be called with a string argument.
def test_StringBalance():
    StringBalance('abc')

# With a non-bracket string
def test_StringBalanceString():
    assert StringBalance('abc') == True

# With a single unbalanced bracket string using a parenthesis
def test_StringBalanceOpenParenthesis():
    assert StringBalance('(abc') == False

def test_StringBalanceOpenParenthesis2():
    assert StringBalance('(abc)') == True

def test_StringBalanceOpenParenthesis3():
    assert StringBalance('(a(b(c)') == False

def test_StringBalanceOpenParenthesis4():
    assert StringBalance(')abc') == False

def test_StringBalanceOpenParenthesis5():
    assert StringBalance('abc)') == False

def test_StringBalanceOpenParenthesis6():
    assert StringBalance('({[)}]') == False

def StringBalance(MyString):
    brackets='()[]{}<>'
    closer_of={
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    openers=closer_of.keys()
    closers=closer_of.values()
    parenthesis = Stack()
    bracket = Stack()
    accolade = Stack()
    for char in MyString:
        print('Char: ', char, parenthesis.items, bracket.items, accolade.items)
        if char in brackets:
            if char == '(':
                parenthesis.push(char)
            elif char in ')':
                if parenthesis.isEmpty():
                    print("exit parenthesis")
                    return False
                else:
                    # if peek is (
                    TopOfStack = parenthesis.pop()
                    if char != closer_of[TopOfStack]:
                        return False
            elif char == '[':
                bracket.push(char)
            elif char == ']':
                if bracket.isEmpty():
                    print("exit bracket")
                    return False
                else:
                    bracket.pop()
            elif char == '{':
                accolade.push(char)
            elif char == '}':
                if accolade.isEmpty():
                    print("exit accolade")
                    return False
                else:
                    accolade.pop()
    if not parenthesis.isEmpty():
        print("exit non-empty parenthesis")
        return False
    elif not bracket.isEmpty():
        print("exit non-empty bracket")
        return False
    elif not accolade.isEmpty():
        print("exit non-empty accolade")
        return False
    else:
        return True
