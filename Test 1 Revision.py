#q1
def create_string_len_tuple(words):
    list_of_tuples = [(word, len(word)) for word in words]
    return list_of_tuples

#q2
# row_prompt = "Enter number of rows: "
# column_prompt = "Enter number of columns: "
#
# rows = int(input(row_prompt))
# columns = int(input(column_prompt))
#
# for row in range(rows - 1, -1, -1):
#     print(" " * row, end="")
#     for column in range(columns):
#         print("*",end="")
#     print()

#q3
def create_surnames_dictionary(names):
    new_dict = {}
    names.sort()
    for name in names:
        space_index = name.find(" ")
        if name[space_index + 1] in new_dict:
            new_dict[name[space_index + 1]].append(name)
        else:
            new_dict[name[space_index + 1]] = [name]
    return new_dict

#q4
# prompt = "Enter a filename: "
# filename = input(prompt)
# read_file = open(filename,'r')
# contents = read_file.read()
# read_file.close()
#
# contents = contents.split()
# new_list = []
#
# for full_name in contents:
#     comma_index = full_name.find(",")
#     new_name = full_name[comma_index + 1: ] + " " + full_name[ :comma_index]
#     new_list.append(new_name)
# print(new_list)

#q5
# prompt = "Enter a filename: "
# filename = input(prompt)
# try:
#     read_file = open(filename,'r')
#     contents = read_file.read()
#     read_file.close()
#
#     contents = contents.split()
#     new_list = []
#
#     for full_name in contents:
#         try:
#             comma_index = full_name.find(",")
#             if comma_index == 0 or comma_index == -1:
#                 raise ValueError
#             new_name = full_name[comma_index + 1: ] + " " + full_name[ :comma_index]
#             new_list.append(new_name)
#         except (IndexError, ValueError):
#             pass
#     print(new_list)
# except FileNotFoundError:
#     print("ERROR: The file '{}' does not exist.".format(filename))

#q6
def rate(n):
    total = 0
    i = 1
    count = 2
    count += 1
    while i < n:
        count +=1
        j = 0
        count += 1
        while j < n:
            count+= 1
            total += j
            count += 1
            j += 1
            count += 1
        count += 1
        i *= 2
        count += 1
    count += 1
    return print("Number of operations: {}".format(count))

#q7
class MyTriangle:
    def __init__(self, side_a=1.0, side_b=1.0, side_c=1.4):
        self.__side_a = float(side_a)
        self.__side_b = float(side_b)
        self.__side_c = float(side_c)

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def get_side_c(self):
        return self.__side_c

    def set_side_a(self, value):
        if float(value) > 0:
            self.__side_a = float(value)

    def set_side_b(self, value):
        if float(value) > 0:
            self.__side_b = float(value)

    def set_side_c(self, value):
        if float(value) > 0:
            self.__side_c = float(value)

    def __str__(self):
        return "The sides of a triangle are: {:.1f}, {:.1f}, {:.1f}.".format(self.__side_a, self.__side_b, self.__side_c)

    def get_area(self):
        import math
        s = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c))

    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    def is_valid(self):
        if (self.__side_a + self.__side_b) > self.__side_c and (self.__side_b + self.__side_c) > self.__side_a and (self.__side_a + self.__side_c) > self.__side_b:
            return True
        return False

#q9
class Rugby:
    def __init__(self, country_name="N/A", points=0):
        self.__country_name = country_name
        self.__points = points

    def get_country_name(self):
        return self.__country_name

    def get_points(self):
        return self.__points

    def __str__(self):
        return "Country: {}({})".format(self.__country_name, self.__points)

#q10
def read_rugby_list(filename):
    try:
        read_file = open(filename, 'r')
        contents = read_file.read()
        read_file.close()

        contents = contents.split("\n")
        new_list = []

        for elements in contents:
            comma_index = elements.find(",")
            country_name = elements[:comma_index]
            points = elements[comma_index + 1:]
            new_object = Rugby(country_name, points)
            new_list.append(new_object)
        return new_list

    except FileNotFoundError:
        print("ERROR: The file '{}' does not exist.".format(filename))
        pass
        return [" "]

#q11
def selection_sort(data):
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        #list indexing
        for i in range(1, pass_num+1):
            if data[i].get_points() > data[position_largest].get_points():
                position_largest = i
            elif data[i].get_points() == data[position_largest].get_points():
                if data[i].get_country_name() > data[position_largest].get_country_name():
                    position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]
    return

#q12
def check_binary_search(sorted_rugby_list, search_country_name):
    max_index = len(sorted_rugby_list) - 1
    min_index = 0
    count = 0
    while (sorted_rugby_list[min_index].get_country_name() <= sorted_rugby_list[max_index].get_country_name()):
        mid_index = (max_index + min_index) // 2
        count += 1
        if sorted_rugby_list[mid_index].get_country_name() == search_country_name:
            return count
        elif sorted_rugby_list[mid_index].get_country_name() < search_country_name:
            min_index = mid_index + 1
        elif sorted_rugby_list[mid_index].get_country_name() > search_country_name:
            max_index = mid_index - 1
    return -1

#q13
def binary_search_tuples(my_list, a):
    # mid = len(my_list) // 2
    # print(mid)
    # num_steps = 0
    # if len(my_list) == 0:
    #     return -1, 0
    # elif a == my_list[mid]:
    #     num_steps += 1
    #     return mid, num_steps
    # elif a > my_list[mid]:
    #     num_steps += 1
    #     for pos in range(mid, len(my_list)):
    #         if my_list[pos] == a:
    #             return pos, num_steps
    #         # num_steps += 1
    # elif a < my_list[mid]:
    #     for pos in range(mid, -1, -1):
    #         if my_list[pos] == a:
    #             return pos, num_steps
    #         num_steps += 1
    # return -1, num_steps
    pass

#q14
def trinary_search(my_list, x):
    if len(my_list) == 0:
        pos = -1
        list_of_midpoints = []
        return pos, list_of_midpoints
    left = 0
    right = len(my_list) - 1
    mid1 = left + (right - left) // 3
    list_of_midpoints = []

    list_of_midpoints.append(mid1)
    if x == my_list[mid1]:
        pos = mid1
        return pos, list_of_midpoints
    elif x < my_list[mid1]:
        for elements in my_list[:mid1]:
            list_of_midpoints.append(my_list.index(elements))
            if x == elements:
                pos = my_list.index(elements)
                return pos, list_of_midpoints
        pos = -1
        return pos, list_of_midpoints
    mid2 = right - (right - left) // 3
    list_of_midpoints.append(mid2)
    if x > my_list[mid1]:
        if x == my_list[mid2]:
            pos = mid2
            return pos, list_of_midpoints
        elif x < my_list[mid2]:
            for elements in my_list[mid1 + 1 : mid2]:
                list_of_midpoints.append(my_list.index(elements))
                if elements == x:
                    pos = my_list.index(elements)
                    return pos, list_of_midpoints
                if x > elements:
                    list_of_midpoints.append(my_list.index(elements))
                    pos = -1
                    return pos, list_of_midpoints
            pos = -1
            return pos, list_of_midpoints
        elif x > my_list[mid2]:
            for elements in my_list[mid2 + 1:]:
                list_of_midpoints.append(my_list.index(elements))
                if elements == x:
                    pos = my_list.index(elements)
                    return pos, list_of_midpoints
                if elements > x:
                    pos = -1
                    return pos, list_of_midpoints
            pos = -1
            return pos, list_of_midpoints
    return

#q15
def find_k_smallest_elements(data, k):
    num_comparisons = 0
    num_swaps = 0
    for pass_num in range(len(data)-1, 0, -1):
        position_smallest = 0
        for i in range(1, pass_num+1):
            if data[i] < data[position_smallest]:
                position_smallest = i
            num_comparisons += 1
        data[position_smallest], data[i] = data[i], data[position_smallest]
        num_swaps += 1
    k_smallest_items = data[-k:]
    return k_smallest_items, num_comparisons, num_swaps

def main():
    data = [1]
    print(find_k_smallest_elements(data, 1))
    data = [1, 2]
    print(find_k_smallest_elements(data, 1))
    data = [1, 2]
    print(find_k_smallest_elements(data, 2))
    data = [1, 2, 3]
    print(find_k_smallest_elements(data, 3))
    data = [1, 3, 2, 4]
    print(find_k_smallest_elements(data, 2))
    data = [1, 3, 2, 5, 4]
    print(find_k_smallest_elements(data, 3))

    data = [3, 2, 1]
    print(find_k_smallest_elements(data, 3))
    data = [3, 2, 1]
    print(find_k_smallest_elements(data, 2))
    data = [1, 2, 3]
    print(find_k_smallest_elements(data, 1))
    # my_list = []
    # a = (3, 1)
    # print(binary_search_tuples(my_list, a))
    #
    # my_list = [(1, 5)]
    # a = (3, 1)
    # print(binary_search_tuples(my_list, a))
    #
    # my_list = [(3, 1)]
    # a = (3, 1)
    # print(binary_search_tuples(my_list, a))
    #
    # my_list = [(1, 5), (1, 7), (2, 1), (2, 5), (3, 1), (3, 5)]
    # a = (3, 1)
    # print(binary_search_tuples(my_list, a))
    #
    # my_list = [(1, 5), (1, 7), (2, 1), (2, 5), (3, 1), (3, 5)]
    # a = (2, 2)
    # print(binary_search_tuples(my_list, a))
    #
    # my_list = [(1, 3), (1, 4), (1, 7), (2, 1), (2, 5), (3, 1), (3, 5), (4, 1), (4, 4)]
    # a = (1, 4)
    # print(binary_search_tuples(my_list, a))
    return

main()