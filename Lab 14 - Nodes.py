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

#6-10 using Node implementation from CodeRunner
def create_sample_node_chain():
    nodes_node = Node('nodes')
    linked_node = Node('linked', nodes_node)
    three_node = Node('three', linked_node)
    return three_node

def print_node_chain(node_of_chain):
    if node_of_chain.get_next() == None:
        return print(node_of_chain.get_data())
    else:
        print(node_of_chain.get_data())
        print_node_chain(node_of_chain.get_next())

def create_node_chain(values):
    if len(values) == 1:
        return Node(values[0])
    else:
        first_node = Node(values[0])
        next_node = create_node_chain(values[1:])
        first_node.set_next(next_node)
        return first_node

def convert_to_list(first_node):
    if first_node.get_next() == None:
        return [first_node.get_data()]
    return [first_node.get_data()] + convert_to_list(first_node.get_next())

def get_consecutive_sum(first_node):
    if first_node.get_next() == None:
        return [first_node.get_data()]
    else:
        current_node = [first_node.get_data()]
        next_node = get_consecutive_sum(first_node.get_next())
        sum = current_node[0] + next_node[0]
        return [sum] + next_node

def main():
    node1 = Node(4)
    node2 = Node(3, node1)
    node3 = Node(2, node2)
    node4 = Node(1, node3)
    print_node_chain(node4)
    print(get_consecutive_sum(node4))

    node1 = Node(5)
    node2 = Node(10, node1)
    node3 = Node(30, node2)
    node4 = Node(40, node3)
    print(get_consecutive_sum(node4))
    return

main()