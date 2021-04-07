class Deque:
    def __init__(self):
        self.__items = []

    def __str__(self):
        print_list = list(self.__items) #copies self.__items separately
        print_list.reverse()
        return f"Deque: {print_list}"

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def is_empty(self):
        if self.__items == []:
            return True
        return False

    def add_front(self, element):
        self.__items.append(element)

    def add_rear(self, element):
        self.__items.insert(0, element)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items.pop()

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items.pop(0)

    def peek_front(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items[-1]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("ERROR: The deque is empty!")
        return self.__items[0]


def main():
    a_deque = Deque()
    a_deque.add_front(1)
    a_deque.add_front(2)
    a_deque.add_front(3)
    a_deque.add_front(4)
    a_deque.add_rear(100)
    a_deque.add_rear(200)
    print(a_deque)
    print(a_deque.peek_front())
    print(a_deque.peek_rear())
    print(a_deque)

    try:
        a_deque = Deque()
        a_deque.add_front(1)
        a_deque.add_front(2)
        print(a_deque.remove_front())
        print(a_deque.remove_front())
        print(a_deque.peek_front())
    except IndexError as error:
        print(error)
    return

main()