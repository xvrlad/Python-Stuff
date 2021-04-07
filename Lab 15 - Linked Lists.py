class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def __str__(self):
        return f"{self.__data}"

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

    def add_after(self, value):
        new_node = Node(value)
        nodes_after = self.get_next()
        self.set_next(new_node)
        new_node.set_next(nodes_after)

    def remove_after(self):
        node_after = self.get_next()
        self.set_next(node_after.get_next())

    def __contains__(self, value):
        if self.get_data() == value:
            return True
        elif self.get_next() != None:
            return self.get_next().__contains__(value)

    def get_sum(self):
        if self.get_next() == None:
            return self.get_data()
        return self.get_data() + self.get_next().get_sum()

class LinkedList:
    def __init__(self):
        self.__head = None

    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.__head)
        self.__head = new_node

    def size(self):
        current = self.__head
        count = 0
        if current == None:
            return count
        current = current.get_next()
        count += 1
        while current != None:
            current = current.get_next()
            count += 1
        return count

    def get_head(self):
        return self.__head

    def clear(self):
        self.__head = None

    def is_empty(self):
        if self.__head == None:
            return True
        return False

    def __len__(self):
        return self.size()

    def __str__(self):
        return_string = "["
        current = self.get_head()
        while current != None:
            return_string = return_string + f"{current}"
            # print(f"{current}, ", end= "")
            current = current.get_next()
            if current == None:
                return return_string + "]"
            return_string += ", "
        return return_string + "]"

    def __contains__(self, search_value):
        current = self.__head
        if current == None:
            return
        while current.get_data() != search_value:
            current = current.get_next()
            if current == None:
                return
        return True

    def __getitem__(self, index):
        list_index = 0
        current = self.__head
        while list_index != index:
            list_index += 1
            current = current.get_next()
        return current

    def add_all(self, a_list):
        for elements in a_list:
            self.add(elements)

    def get_min_odd(self):
        if len(self) == 0:
            return 999
        smallest_odd = 999
        for i in range(1, len(self)):
            if self.__getitem__(i).get_data() < smallest_odd and self.__getitem__(i).get_data() % 2 != 0:
                smallest_odd = self.__getitem__(i).get_data()
        return smallest_odd

    def reverse(self):
        previous = None
        current = self.get_head()
        for iterations in range(len(self)):
            next_node = current.get_next()
            current.set_next(previous)
            previous = current
            current = next_node
        self.__head = previous

    def __iter__(self):
        return LinkedListIterator(self.__head)

class SquareNumber:
    def __init__(self, count=5):
        self.__count = count

    def __iter__(self):
        return SquareNumberIterator(self.__count)

class SquareNumberIterator:
    def __init__(self, count):
        self.__current = 1
        self.__count = count

    def __next__(self):
        if self.__current > self.__count:
            raise StopIteration
        current = self.__current ** 2
        self.__current += 1
        return current

class LinkedListIterator:
    def __init__(self, head):
        self.__current = head

    def __next__(self):
        if self.__current == None:
            raise StopIteration
        current = self.__current
        self.__current = self.__current.get_next()
        return current

def main():
    values = LinkedList()
    values.add('cherry')
    values.add('banana')
    values.add('apple')
    for value in values:
        print(value)

    values = LinkedList()
    values.add(1)
    values.add(2)
    values.add(3)
    for value in values:
        print(value)
    return

main()