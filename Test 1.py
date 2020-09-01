#q1
def generate_polynomial_sequence(n):
    new_list = []
    for x in range(0,n):
        polynomial = (4 * x**2) - (2 * x) - 4
        new_list.append(polynomial)
    return new_list

#q2
def create_string_ascii_mean_tuple(words):
    new_list = []
    for word in words:
        character_list = list(word)
        average = 0
        for character in character_list:
            average += ord(character)
        average /= len(word)
        new_tuple = word, round(average,1)
        new_list.append(new_tuple)
    return new_list

#q3
def merge_into_one(list_of_lists):
    merged_list = []
    for lists in list_of_lists:
        for elements in lists:
            merged_list.append(elements)
    return merged_list

#q4
def repeated_counts_even(numbers):
    new_dict = {}
    new_list = []
    count = 0
    numbers.sort()
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    for num in new_list:
        i = 0
        while i < len(numbers):
            if numbers[i] == num:
                count += 1
            i += 1
        if count % 2 == 0:
            new_dict[num] = count
        count = 0
    return new_dict



    # new_list = []
    # store_number = []
    # count = 1
    # new_dict = {}
    # for number in numbers:
    #     if number not in new_list:
    #         new_list.append(number)
    #     else:
    #         count += 1
    pass

#q5
def median(values):
    find_9999 = values.index(9999)
    new_list = values[:find_9999]
    new_list.sort()
    if find_9999 == 0:
        median = None
        return median
    elif len(new_list) % 2 != 0:
        median = new_list[len(new_list) // 2]
    elif len(new_list) % 2 == 0:
        left_mid = len(new_list) // 2
        right_mid = left_mid - 1
        numerator = new_list[left_mid] + new_list[right_mid]
        median = numerator / 2
        median = round(median)
    return median

#q6
def print_histogram(a_list_of_lists):
    x = "X"
    histogram_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for list in a_list_of_lists:
        for number in list:
            histogram_dict[number] += 1
    for keys, values in histogram_dict.items():
        print("{}: ".format(keys) + x * values)
    return

#q7
def rate(n):
    count = 0

    total = 0
    for i in range(10):
        total += i
    i = 1
    while i < n:
        count += 1
        j = 0
        count += 1
        while j < n:
            count += 1
            k = 0
            count += 1
            while k < 10:
                count += 1
                total += k
                count += 1
                k += 2
                count += 1
            count += 1
            j += 1
            count += 1
        count += 1
        i *= 2
        count += 1
    return print("Number of operations:", count)

#q8
# age_prompt = "Enter your age: "
# months_prompt = "Enter the number of months you have lived in NZ: "
# try:
#     age = int(input(age_prompt))
#     if age < 0:
#         raise ValueError
#     months = int(input(months_prompt))
#     if months < 0:
#         raise ValueError
#     elif age >= 18 and months >= 12:
#         print("You are eligible to enrol and vote in the upcoming election.")
#     else:
#         print("You are NOT eligible to enrol and vote in the upcoming election.")
#
# except TypeError:
#     print("Invalid input!")
# except ValueError:
#     print("Invalid input!")

#q9
def print_bmi_list(filename):
    try:
        result = []
        input_file = open(filename, "r")
        content = input_file.readlines()
        for line in content:
            try:
                if len(line) > 0:
                    name, weight, height = line.split(",")
                    bmi = float(weight) / (float(height) * float(height))
                    result.append((name, bmi))
            except ValueError:
                pass
        input_file.close()
        for value in result:
            print("{}, bmi={:.1f}".format(value[0], value[1]))
    except FileNotFoundError:
        return print("ERROR: The file '{}' does not exist.".format(filename))
    return

#q10/q11
def bubble_sort_descending(data):
    """Sorts a list into descending order"""

    comparisons = 0
    swaps = 0

    n = len(data)
    for i in range(n):
        for j in range(n - 1, i, -1) :
            comparisons += 1
            if data[j - 1] < data[j] :
                data[j - 1], data[j] = data[j], data[j - 1]
                swaps += 1
    if swaps == 0:
        comparisons = len(data) - 1
    return comparisons, swaps

#q12
def binary_search_function_maximum(list_of_f_values):
    N = len(list_of_f_values)
    left_index = 0
    right_index = N - 1
    middle_index = (left_index + right_index) // 2
    count_middle_index_computations = 1
    found_maximum = False

    while not found_maximum:
        x1 = list_of_f_values[left_index]
        x2 = list_of_f_values[right_index]
        indexed_value = list_of_f_values[middle_index]

        if indexed_value > x1 and indexed_value > x2:
            found_maximum = True
        # elif indexed_value > x1 and indexed_value < x2:
        #     left_index += 1
        # elif indexed_value > x2:
        #     right_index -= 1
        
        middle_index = (left_index + right_index) // 2
        count_middle_index_computations += 1
    return middle_index, count_middle_index_computations

    # N = len(list_of_f_values)
    # left_index = 0
    # right_index = N - 1
    # middle_index = (left_index + right_index) // 2
    # count_middle_index_computations = 1
    # found_maximum = False
    # while not found_maximum:
    #     count_middle_index_computations += 1
    #     print(left_index, middle_index, right_index)
    #     if list_of_f_values[left_index] < list_of_f_values[right_index]:
    #         right_index -= 1
    #     elif list_of_f_values[left_index] > list_of_f_values[right_index]:
    #         left_index += 1
    #     elif list_of_f_values[left_index] < list_of_f_values[middle_index] and list_of_f_values[middle_index] > list_of_f_values[right_index]:
    #         found_maximum = True
    #     middle_index = (left_index + right_index) // 2
    # return middle_index, count_middle_index_computations

def main():
    list_of_f_values = [0, 1, 11, 3]
    (index, nr_of_computations) = binary_search_function_maximum(list_of_f_values)
    print("Found maximum at index {}, number of middle index computations = {}".format(index, nr_of_computations))
    list_of_f_values = [0, 11, 3, 1]
    (index, nr_of_computations) = binary_search_function_maximum(list_of_f_values)
    print("Found maximum at index {}, number of middle index computations = {}".format(index, nr_of_computations))
    list_of_f_values = [1, 2, 3, 5, 9, 13, 21, 32, 47, 60, 76, 88, 97, 100, 97, 88, 76, 60, 47, 32, 21, 13]
    (index, nr_of_computations) = binary_search_function_maximum(list_of_f_values)
    print("Found maximum at index {}, number of middle index computations = {}".format(index, nr_of_computations))
    return

main()
