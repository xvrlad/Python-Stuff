class SimpleHashTable:
    def __init__(self, integer=7):
        self.__size = integer
        self.__slots = [None] * self.__size

    def __str__(self):
        return f"{self.__slots}"

    def get_hash_code(self, key):
        return key % self.__size

    def get_size(self):
        return self.__size

    def put(self, key):
        index = self.get_hash_code(key)
        if self.__slots[index] != None:
            index = self.get_new_hash_code_linear_probing(index)
            if index == None:
                raise IndexError("ERROR: The hash table is full.")
        self.__slots[index] = key

    def __len__(self):
        count = 0
        for elements in self.__slots:
            if elements != None:
                count += 1
        return count

    def get_new_hash_code_linear_probing(self, index):
        index_initial = index
        while self.__slots[index] != None:
            index += 1
            index = index % self.__size
            if index == index_initial:
                return None
        return index

    def is_empty(self):
        if [None] * self.__size == self.__slots:
            return True
        return False

    def clear(self):
        self.__slots = [None] * self.__size

    def rehashing(self, new_size):
        get_original_elements = [element for element in self.__slots if element is not None]
        self.__slots = [None] * new_size
        self.__size = new_size
        for element in get_original_elements:
            self.put(element)

class QuadraticHashTable:
    def __init__(self, integer=7):
        self.__size = integer
        self.__slots = [None] * self.__size

    def __str__(self):
        return f"{self.__slots}"

    def get_hash_code(self, key):
        return key % self.__size

    def get_size(self):
        return self.__size

    def put(self, key):
        index = self.get_hash_code(key)
        if self.__slots[index] != None:
            index = self.get_new_hash_code_quadratic_probing(index, 0)
            if index == None:
                raise IndexError("ERROR: The hash table is full.")
        self.__slots[index] = key

    def __len__(self):
        count = 0
        for elements in self.__slots:
            if elements != None:
                count += 1
        return count

    def is_empty(self):
        if [None] * self.__size == self.__slots:
            return True
        return False

    def clear(self):
        self.__slots = [None] * self.__size

    def rehashing(self, new_size):
        get_original_elements = [element for element in self.__slots if element is not None]
        self.__slots = [None] * new_size
        self.__size = new_size
        for element in get_original_elements:
            self.put(element)

    def get_new_hash_code_quadratic_probing(self, index, distance):
        index_initial = index
        while self.__slots[index] != None:
            distance += 1
            index = (index_initial + (distance ** 2)) % self.__size
            if index == index_initial:
                return None
        return index

class DoubleHashTable:
    def __init__(self, size=7, second_hash_value=5):
        self.__size = size
        self.__second_hash_value = second_hash_value
        self.__slots = [None] * self.__size

    def __str__(self):
        return f"{self.__slots}"

    def get_hash_code(self, key):
        return key % self.__size

    def get_size(self):
        return self.__size

    def put(self, key):
        index = self.get_hash_code(key)
        if self.__slots[index] != None:
            initial_index = index
            step_size = self.get_new_hash_code_double_hashing(key)
            step = 0
            while self.__slots[index] != None:
                step += 1
                index = (initial_index + step * step_size) % self.__size
        self.__slots[index] = key

    def __len__(self):
        count = 0
        for elements in self.__slots:
            if elements != None:
                count += 1
        return count

    def is_empty(self):
        if [None] * self.__size == self.__slots:
            return True
        return False

    def clear(self):
        self.__slots = [None] * self.__size

    def rehashing(self, new_size):
        get_original_elements = [element for element in self.__slots if element is not None]
        self.__slots = [None] * new_size
        self.__size = new_size
        for element in get_original_elements:
            self.put(element)

    def get_new_hash_code_double_hashing(self, key):
        secondary_hash_function = self.__second_hash_value - (key % self.__second_hash_value)
        return secondary_hash_function

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

class LinkedListHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [LinkedList() for i in range(self.__size)] #implementing it like this means that every linked list inside self.__slots has its own reference

    def get_hash_code(self, key):
        return key % self.__size

    def __str__(self):
        for elements in range(len(self.__slots) - 1):
            print(self.__slots[elements])
        return f"{self.__slots[-1]}"

    def put(self, key):
        hash_index = self.get_hash_code(key)
        self.__slots[hash_index].add(key)

    def __len__(self):
        count = 0
        for linked_list in self.__slots:
            count += linked_list.size()
        return count
    
def main():
    hash_table = QuadraticHashTable(5)
    hash_table.put(3)
    hash_table.put(6)
    hash_table.put(9)
    hash_table.put(11)
    hash_table.put(21)
    # hash_table.put(13)
    print(hash_table)
    print("The linked list hash table contains {} items.".format(len(hash_table)))
    return

main()