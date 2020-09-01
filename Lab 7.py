#q1
def insertion_sort(data):	
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1

        while i >= 0 and data[i][1] < item_to_insert[1]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = item_to_insert
    return

#q2
def double(my_list):
    for index in range(len(my_list)):
        my_list[index] *= 2
    return

#q3
def get_middle_number(numbers):
    numbers.sort()
    middle_number_index = len(numbers) // 2
    return numbers[middle_number_index]
    
#q4 and 5
def get_middle_number_from_file(filename):
    try:
        read_file = open(filename, 'r')
        contents = read_file.read()
        read_file.close()

        contents = contents.split()
        new_list = []
        
        for elements in contents:
            try:
                if contents == []:
                    raise TypeError
                elif not elements.isdigit():
                    raise ValueError
                new_list.append(elements)
            except ValueError:
                print('ERROR: "{}" contains an invalid value.'.format(filename))
        if new_list == []:
            raise TypeError
        new_list = [int(integers) for integers in new_list]
    except FileNotFoundError:
        return 'ERROR: "{}" does not exist.'.format(filename)
    except TypeError:
        return 'ERROR: "{}" is empty.'.format(filename)
    return get_middle_number(new_list)

#q6
def linear_search(student_id, students):
    for elements in students:
        if student_id == elements[0]:
            return elements[1]
    return

#q7
def get_unique_letters(word_a, word_b):
    result = []
    for letter in word_a:
        if letter not in word_b and letter not in result:
            result.append(letter)
    for letter in word_b:
        if letter not in word_a and letter not in result:
            result.append(letter)
    return ''.join(sorted(result))

#q8
def rotate_4(numbers):
    if len(numbers) <= 4:
        return numbers
    new_list = numbers[4:] + numbers[0:4]
    return new_list

#q9
def get_list_of_odd_maximums(a_list_of_lists):
    max_list = []
    return_list = []
    for lists in a_list_of_lists:
        for integers in lists:
            if integers % 2 != 0:
                max_list.append(integers)
        try:
            return_list.append(max(max_list))
        except ValueError:
            return_list.append(None)
        max_list = []
    return return_list

#q10
def draw_triangle(size=5):
    try:
        x = "X"
        dash = "-"
        space = " "
        if size < 3:
            raise ValueError
        if size % 2 == 0:
            number_of_spaces = (size // 2) - 1
            number_of_symbols = 2
            top_row = space * number_of_spaces + x * number_of_symbols + space * number_of_spaces
            in_between_range = (size // 2) - 2
            print(top_row)
            for rows_between in range(in_between_range):
                number_of_spaces -= 1
                print(space * number_of_spaces + x + dash * number_of_symbols + x)
                number_of_symbols += 2
        else:
            number_of_spaces = size // 2
            number_of_symbols = 1
            top_row = space * number_of_spaces + x + space * number_of_spaces
            in_between_range = (size // 2) - 1
            print(top_row)
            for rows_between in range(in_between_range):
                number_of_spaces -= 1
                print(space * number_of_spaces + x + dash * number_of_symbols + x)
                number_of_symbols += 2
        bottom_row = x * size
        print(bottom_row)
    except ValueError:
        print("ERROR: The size is too small.")
    except TypeError:
        print("ERROR: Invalid input!")
    return

#q11
def get_position_of_highest(data, index):
    list_part = data[: index + 1]
    greatest_letter = max(list_part)
    return list_part.index(greatest_letter)

def selection_row(data, index):
    greatest_letter = data[get_position_of_highest(data, index)]
    swap_letter = data[index]

    data[index] = greatest_letter
    data[get_position_of_highest(data, index)] = swap_letter
    return 

def my_selection_sort(data):
    sort_data = sorted(data)
    for pass_num in range(len(data)-1, 0, -1):
        selection_row(data, pass_num)
    return 

def swaps(numbers):
    my_selection_sort(numbers)
    print(numbers)
    return 

#q12
def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    count = 0
    while (min_index <= max_index):
        mid_index = (max_index + min_index) // 2
        if numbers[mid_index][0] == value:
            count += 1
            return count
        elif numbers[mid_index][0] < value:
            min_index = mid_index + 1
        elif numbers[mid_index][0] > value:
            max_index = mid_index - 1
        count += 1
    return -1
def check_count(student_id, students):
    count = binary_search(sorted(students), student_id)
    return count

def main():
    numbers = [0, 4, 2, 7, 5]
    print(swaps(numbers))
    numbers = [5, 2, 1, 8, 0, 3, 7]
    print(swaps(numbers))
    numbers = [9, 8, 7, 6, 5, 4]
    print(swaps(numbers))
    numbers = [5,4,3,2]
    print(swaps(numbers))
    numbers = [0, 1, 2, 3, 4, 5]
    print(swaps(numbers))
    return

main()
