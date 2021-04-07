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

class OrderedLinkedList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        if self.__head == None:
            return True
        return False

    def add(self, value):
        new_node = Node(value)
        previous = None
        if self.is_empty():
            self.__head = new_node
        current = self.__head
        print(current)
        # while new_node.get_data() > current.get_data():
        #     previous = current
        #     current = current.get_next()
        #     if new_node.get_data() < self.__head.get_data():
        #         next_node = self.__head
        #         self.__head = new_node
        #         new_node.set_next(next_node)
        #     elif current == None:
        #         previous.set_next(new_node)
        #     elif previous != None and new_node.get_data() < current.get_data():
        #         new_node.set_next(current)
        #         previous.set_next(new_node)

    def __str__(self):
        return f"[{self.__head}]"

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

def main():
    values = OrderedLinkedList()
    values.add('c')
    values.add('b')
    values.add('a')
    print(values)

    values = OrderedLinkedList()
    values.add(1)
    values.add(2)
    print(values)
    return

main()