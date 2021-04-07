def running_sum_over_12(numbers):
    sum = 0
    for number in numbers:
        sum += number
        if sum > 12:
            return sum
    return -1


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return round(self.__width * self.__height)

    def set_height(self, new_height):
        self.__height = new_height

    def set_width(self, new_width):
        self.__width = new_width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def __str__(self):
        return f"Rectangle: {self.__width}cm (width) x {self.__height}cm (height)"


class Cipher:
    def __init__(self, offset, reverse):
        self.__offset = offset
        self.__reverse = reverse

    def encode(self, word):
        character_list = list(word)
        for index in range(len(character_list)):
            encode_character = (ord(character_list[index]) + self.__offset)
            if encode_character > 122:
                encode_character = 96 + abs(encode_character - 122)
            elif encode_character < 97:
                encode_character = 123 - abs(encode_character - 97)
            character_list[index] = chr(encode_character)
        if self.__reverse is True:
            character_list.reverse()
        return ''.join(character_list)

    def decode(self, word):
        character_list = list(word)
        for index in range(len(character_list)):
            decode_character = (ord(character_list[index]) - self.__offset)
            if decode_character > 122:
                decode_character = 96 + abs(decode_character - 122)
            elif decode_character < 97:
                decode_character = 123 - abs(decode_character - 97)
            character_list[index] = chr(decode_character)
        if self.__reverse is True:
            character_list.reverse()
        return ''.join(character_list)


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: {} <- top of the stack'.format(str(self.__items))

    def slice(self, start, stop, step=1):
        new_stack = Stack()
        if self.is_empty():
            return new_stack
        for iterations in range(start, stop, step):
            new_stack.push(self.__items[iterations])
        return new_stack


class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[self.size() - 1]

    def __str__(self):
        return 'Queue: front->{}<- end'.format(str(self.__items[::-1]))

    def splice(self, second_queue):
        self.__items = second_queue.__items + self.__items


def create_chain(elements):
    if elements == []:
        return None
    new_node = Node(elements[0])
    new_node.set_next(create_chain(elements[1:]))
    return new_node


class LinkedList:
    def __init__(self):
        self.__head = None

    def add(self, item):  # add to the beginning of the list
        new_node = Node(item, self.__head)
        self.__head = new_node

    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def is_empty(self):
        return self.__head == None

    def __str__(self):
        result = "["
        separator = ""
        current = self.__head
        while current != None:
            result += separator + str(current.get_data())
            separator = ", "
            current = current.get_next()
        result += "]"
        return result

    def has_same_elements(self, list2):
        if self.__head is None and list2 is None:
            return True


def evaluate_f(num):
    if num == 0:
        return 2
    total = 3
    if num % 2 == 0:
        total += evaluate_f(num - 2)
    elif num % 2 != 0:
        total = 0 + evaluate_g(num) + evaluate_f(num - 1)
    return total


def evaluate_g(num):
    if num == 1:
        return 3
    total = -2
    if num % 2 == 0:
        total = evaluate_f(num) * evaluate_g(num - 1)
    elif num % 2 != 0:
        total += evaluate_g(num - 2)
    return total


class Folder:
    def __init__(self, folder_name, list_of_subfolders, list_of_filenames):
        self.__name = folder_name
        self.__subfolders = list_of_subfolders
        self.__files = list_of_filenames

    def __str__(self):
        return self.__name

    def get_files(self):
        return self.__files

    def get_subfolders(self):
        return self.__subfolders


def folder_search(folder, file):
    if folder.__files == []:
        return None
    pass


def get_rightmost_data(b_tree):
    if b_tree.get_right() is None:
        return b_tree.get_data()
    return get_rightmost_data(b_tree.get_right())

#q11
def print_leaf_nodes(b_tree):
    if b_tree is None:
        return True
    leaf_node = print_leaf_nodes(b_tree.get_left())
    if leaf_node is True:
        print(b_tree.get_data(), end=' ')
        return
    leaf_node = print_leaf_nodes(b_tree.get_right())
    return

def main():
    val = evaluate_f(3)
    print(val)

    val = evaluate_f(6)
    print(val)

    val = evaluate_f(0)
    print(val)
    return


main()
