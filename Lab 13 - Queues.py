class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.__items[len(self.__items)-1]

    def __str__(self):
        self.__items.reverse()
        return f"Queue: {self.__items}"

    def __len__(self):
        return self.size()

    def clear(self):
        self.__items = []

    def enqueue_list(self, a_list):
        for element in a_list:
            self.enqueue(element)

    def multi_dequeue(self, number):
        if number > self.size():
            return False
        for pops in range(number):
            self.dequeue()
        return True

def mirror_queue(a_queue): #the Queue implementation of CodeRunner is not the same as here.
    helper_queue = Queue()
    helper_stack = Stack()
    for operation in range(a_queue.size()):
        dequeue_element = a_queue.dequeue()
        helper_queue.enqueue(dequeue_element)
        helper_stack.push(dequeue_element)
    for dequeues in range(helper_queue.size()):
        a_queue.enqueue(helper_queue.dequeue())
    for pops in range(helper_stack.size()):
        a_queue.enqueue(helper_stack.pop())
    return

def is_palindrome(word): #so is this one
    new_queue = Queue()
    new_stack = Stack()
    character_list = list(word)
    for character in character_list:
        new_queue.enqueue(character)
        new_stack.push(character)
    for pops in range(new_queue.size()):
        dequeue_element = new_queue.dequeue()
        pop_element = new_stack.pop()
        if dequeue_element != pop_element:
            return False
    return True

#q7-10
class CircularQueue:
    def __init__(self, capacity=8):
        self.__capacity = capacity
        self.__items = [None] * capacity
        self.__front = 0
        self.__back = capacity - 1
        self.__count = 0

    def is_empty(self):
        if self.__count == 0:
            return True
        return False

    def __str__(self):
        return f"{self.__items}, front:{self.__front}, back:{self.__back}," \
               f" count:{self.__count}"

    def is_full(self):
        if self.__count == self.__capacity:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        self.__back = (self.__back + 1) % self.__capacity
        self.__items[self.__back] = item
        self.__count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        front_element = self.__items[self.__front]
        self.__front = (self.__front + 1) % 4
        self.__count -= 1
        return front_element

    def print_all(self):
        sort_list = []
        for element in self.__items[self.__front: ]:
            if element != None:
                sort_list.append(element)
        if self.__front != self.__back and self.__back == 0:
            sort_list.append(self.__items[self.__back])
        sort_list.sort()
        for element in sort_list:
            print(element, end= " ")
        print()

def main():
    q1 = CircularQueue(4)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q1.print_all()
    print(q1.dequeue())
    q1.print_all()

    q1 = CircularQueue(5)
    q1.enqueue(1)
    q1.dequeue()
    q1.enqueue(2)
    q1.enqueue(3)
    q1.dequeue()
    q1.dequeue()
    print(q1)
    q1.print_all()

    q1 = CircularQueue(4)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q1.dequeue()
    q1.enqueue(5)
    print(q1)
    q1.print_all()

    q1 = CircularQueue(4)
    q1.dequeue()
    q1.enqueue(5)
    print(q1)
    q1.print_all()
    return

main()