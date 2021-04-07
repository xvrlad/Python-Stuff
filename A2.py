#q1
def highest_value_word(word1, word2, ordinal_position=1):
    index_position = ordinal_position - 1
    if word1 == word2:
        return 0
    elif index_position == len(word1) or index_position == len(word2):
        return ordinal_position if index_position == len(word1) else -ordinal_position
    elif ord(word1[index_position]) > ord(word2[index_position]):
        return -ordinal_position
    elif ord(word1[index_position]) < ord(word2[index_position]):
        return ordinal_position
    return highest_value_word(word1, word2, ordinal_position + 1)

#q2
class UndoRedo:
    def __init__(self):
        self.__back = Stack()
        self.__forward = Stack()
        self.__current = None

    def get_prev(self):
        if self.__back.is_empty():
            return None
        self.__forward.push(self.__current)
        popped_element = self.__back.pop()
        self.__current = popped_element
        return popped_element

    def get_next(self):
        if self.__forward.is_empty():
            return None
        self.__back.push(self.__current)
        popped_element = self.__forward.pop()
        self.__current = popped_element
        return popped_element

    def add_item(self, data):
        self.__back.push(self.__current)
        self.__current = data
        self.__forward = Stack()

#q3
def selection_order(items, interval):
    item_queue = Queue()
    for elements in items:
        item_queue.enqueue(elements)
    return_list = []
    dequeue_counter = 0
    while len(return_list) != len(items):
        dequeue_item = item_queue.dequeue()
        dequeue_counter += 1
        if dequeue_counter % interval == 0:
            return_list.append(dequeue_item)
        elif dequeue_counter % interval != 0:
            item_queue.enqueue(dequeue_item)
    return return_list

#q4
class Node:

    def __init__(self, data, next=None):

        self.__data = data

        self.__next = next

    def get_data(self):

        return self.__data

    def get_next(self):

        return self.__next

    def set_data(self, new_data):

        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

    def __str__(self):

        return str(self.__data)
class QueueAsLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    def size(self):
        return self.__count
    def enqueue(self, item):
        if self.__head is None:
            self.__head = Node(item)
        elif self.__tail is None:
            self.__tail = Node(item)
            self.__head.set_next(self.__tail)
        else:
            self.__tail.set_next(Node(item))
            self.__tail = self.__tail.get_next()
        self.__count += 1
    def dequeue(self):
        if self.__head is None:
            return None
        current_head = self.__head.get_data()
        self.__head = self.__head.get_next()
        self.__count -= 1
        return current_head
    def peek(self):
        if self.__head is None:
            return None
        return self.__head.get_data()
    def is_empty(self):
        if self.__count == 0:
            return True
        return False

#q5
def hash_string_weighted_folding(string_to_hash, modulus):
    sum = 0
    for character_index in range(len(string_to_hash)):
        sum += (ord(string_to_hash[character_index]) * (256 ** (character_index % 4)))
    return sum % modulus

#q6
def max_value_length(tree):
    if tree is None:
        return 0
    return max(len(str(tree.get_data())), max_value_length(tree.get_left()),
               max_value_length(tree.get_right()))

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, left=self.__left)
            self.__left = tree
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, right=self.__right)
            self.__right = tree
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data
    def set_left(self, left):
        self.__left = left
    def set_right(self, right):
        self.__right = right

def add_all(a_list, index):
    if index == len(a_list) - 1:
        return BinaryTree(a_list[index])
    new_binary_tree = BinaryTree(a_list[index])
    left_child_index = 2 * index + 1
    if left_child_index < len(a_list):
        new_binary_tree.set_left(add_all(a_list, left_child_index))
    right_child_index = 2 * index + 2
    if right_child_index < len(a_list):
        new_binary_tree.set_right(add_all(a_list, right_child_index))
    return new_binary_tree

def convert_tree_to_list(b_tree):
    if b_tree is None:
        return None
    new_list = [b_tree.get_data(), convert_tree_to_list(b_tree.get_left()), convert_tree_to_list(b_tree.get_right())]
    return new_list

#q7
def reverse_sort_order(tree):
    tree_nodes = get_tree_preorder(tree)
    tree_nodes.sort()
    tree_nodes.reverse()
    return tree_nodes

#q8
def get_bst_list_order(tree):
    if tree is None:
        return []
    new_queue = Queue()
    return_list = []
    new_queue.enqueue(tree)
    while not new_queue.is_empty():
        current = new_queue.peek()
        return_list.append(new_queue.dequeue().get_data())
        if current.get_left() is not None:
            new_queue.enqueue(current.get_left())
        if current.get_right() is not None:
            new_queue.enqueue(current.get_right())
    return return_list

class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, left=self.__left)
            self.__left = t
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, right=self.__right)
            self.__right = t
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_left(self, left):
        self.__left = left
    def set_right(self, right):
        self.__right = right
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

    def __contains__(self, value):
        if value == self.get_data():
            return True
        elif value < self.get_data():
            return self.get_left().__contains__(value) if self.get_left() is not None else False
        elif value > self.get_data():
            return self.get_right().__contains__(value) if self.get_right() is not None else False

    def search(self, value):
        if value == self.get_data():
            return self
        elif value < self.get_data():
            return self.get_left().search(value) if self.get_left() is not None else None
        elif value > self.get_data():
            return self.get_right().search(value) if self.get_right() is not None else None

    def insert(self, value):
        if value == self.get_data():
            return #checks if the value is already in the tree
        elif value < self.get_data():
            if self.get_left() is None:
                self.set_left(BinarySearchTree(value)) #creates a link
            else:
                self.get_left().insert(value)
        else:
            if self.get_right() is None:
                self.set_right(BinarySearchTree(value))
            else:
                self.get_right().insert(value)

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

def main():
    new_bt = add_all(["Hoiho", "Kaki", "Takahe", "Ruru", "Moa", "Piwaiwaka"], 0)
    print(convert_tree_to_list(new_bt))
    print(max_value_length(new_bt))
    return

main()