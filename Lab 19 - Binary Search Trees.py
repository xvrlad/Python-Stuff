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

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

def create_bst_from_list(values):
    new_bst = BinarySearchTree(values[0])
    for node in values[1: ]:
        new_bst.insert(node)
    return new_bst

def create_bst_from_sorted(values):
    #root is calculated via the middle index of the list 'values'
    if values == []:
        return
    root = values[len(values) // 2]
    new_bst = BinarySearchTree(root)
    new_bst.set_left(create_bst_from_sorted(values[:len(values) // 2]))
    new_bst.set_right(create_bst_from_sorted(values[(len(values) // 2) + 1 :]))
    return new_bst

def get_bst_preorder(tree):
    # if tree is None:
    #     return
    #
    if tree is None:
        return None
    new_list = [tree.get_data(), get_bst_preorder(tree.get_left()), get_bst_preorder(tree.get_right())]
    return new_list
    # current_node = [tree.get_data()]
    # # print(current_node)
    # left_subtree = get_bst_preorder(tree.get_left())
    # print(left_subtree)
    # get_bst_preorder(tree.get_right())
    # return
    # current_node.append(get_bst_preorder(tree.get_left()))


def main():
    tree2 = create_bst_from_sorted([1, 2, 3, 4, 5, 6])
    print_tree(tree2, 0)

    print(get_bst_preorder(tree2))
    return

main()