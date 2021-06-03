class DEQ():

    def __init__(self):
        self.items = []

    def front_add(self, item):
        self.items.insert(0,item)

    def rear_add(self,item):
        self.items.append(item)

    def front_pop(self):
        if self.items:
            #front = self.items[0]
            #self.items = self.items[1:]
            #return front
            return self.items.pop(0)
        else:
            return None

    def rear_pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def front_peek(self):
        if self.items:
            return self.items[0]
        else:
            return None

    def rear_peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def  size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

def deq_print(deq):
    print('deq.items: ', deq.items)
    print('deq.size(): ', deq.size())
    print('deq.isEmpty(): ', deq.isEmpty())
    print()

def test_createDEQ():
    deq = DEQ()
    deq_print(deq)

    deq.rear_add('apple')
    deq_print(deq)

    deq.front_add('banana')
    deq_print(deq)

    deq.rear_add('carrot')
    deq_print(deq)

    front = deq.front_pop()
    print('front: ', front)
    deq_print(deq)

    rear = deq.rear_pop()
    print('rear: ', rear)
    deq_print(deq)

    deq.front_add('banana')
    deq.rear_add('carrot')
    print('reset')
    deq_print(deq)

    print('peek front: ', deq.front_peek())
    print('peek rear: ', deq.rear_peek())

def test_palindrom():
    deq = DEQ()
    palindrom1 = 'legermeetsysteemregel' # single
    palindrom2 = 'trugtimeinesohellehoseniemitgurt' # double
    palindrom = 'oranges'
    for char in palindrom:
        deq.rear_add(char)
    deq_print(deq)
    pallen=len(palindrom)

    halflen=int(pallen//2)
    doublehalflen=2 * halflen
    print(pallen, halflen)
    print(pallen, doublehalflen)
    print(doublehalflen == pallen)
    if doublehalflen == pallen :
        # double symmetry center element
        print('double')
    else:
        # single symmetry center element
        print('single')
    isAPalindrom=True
    for index in range(0,halflen):
        print(deq.items[index], deq.items[-index-1])
        if deq.items[index] != deq.items[-index-1]:
            print('Not a palindrome')
            isAPalindrom = False
            break
    if isAPalindrom:
        print(palindrom, 'is a pallindrom')