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

def create_a_bigger_tree():
    bigger_tree = BinaryTree('a')
    bigger_tree.insert_left('b')
    bigger_tree.insert_right('c')
    bigger_tree.get_left().insert_left('d')
    bigger_tree.get_left().insert_right('e')
    bigger_tree.get_left().get_left().insert_right('f')
    bigger_tree.get_left().get_right().insert_right('g')
    return bigger_tree

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

def get_height(b_tree):
    if b_tree is None:
        return -1
    return 1 + max(get_height(b_tree.get_left()), get_height(b_tree.get_right()))

def search(tree, item):
    #base case returns False
    if tree is None:
        return False
    #recursive step returns True
    elif tree.get_data() == item:
        return True
    search_time = search(tree.get_left(), item)
    search_time = search(tree.get_right(), item)
    return search_time

def get_sum_string_len(my_tree):
    #base case simply returns 0
    if my_tree is None:
        return 0
    #recursion step sums left/right subtree simultaneously
    return len(my_tree.get_data()) + get_sum_string_len(my_tree.get_left()) + get_sum_string_len(my_tree.get_right())

def convert_tree_to_list(b_tree):
    if b_tree is None:
        return None
    new_list = [b_tree.get_data(), convert_tree_to_list(b_tree.get_left()), convert_tree_to_list(b_tree.get_right())]
    return new_list

def get_min_even(b_tree):
    if b_tree is None:
        return 9999
    min_even = b_tree.get_data() if b_tree.get_data() % 2 == 0 else 9999
    left_side = get_min_even(b_tree.get_left())
    min_even = min(min_even, left_side)
    right_side = get_min_even(b_tree.get_right())
    min_even = min(min_even, right_side)
    return min_even

def combine_trees(btree1, btree2):
    if btree1 is None or btree2 is None:
        return
    #add values if two nodes overlap
    #get data for both (add) then recurse

def main():
    tree = BinaryTree(12345)
    result = convert_tree_to_list(tree)
    print(result)

    # my_tree = BinaryTree('berry')
    # my_tree.insert_left('apple')
    # my_tree.insert_right('banana')
    # print(get_sum_string_len(my_tree))
    #
    # tree3 = add_all(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 0)
    # print(get_sum_string_len(tree3))
    return

main()