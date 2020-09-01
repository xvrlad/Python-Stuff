#q2
def bubble_row(data, index):
    index1 = 0
    index2 = 1
    
    while index2 <= index:
        first_element = data[index1]
        next_element = data[index2]
        if first_element > next_element:
            data[index1] = next_element
            data[index2] = first_element
        index1 += 1
        index2 += 1
    return

#q3
def my_bubble_sort(data): 
    for pass_num in range(len(data)-1, 0, -1):
        bubble_row(data, pass_num)
    return

#q5
def get_position_of_highest(data, index):
    list_part = data[: index + 1]
    greatest_letter = max(list_part)
    return list_part.index(greatest_letter)

#q6
def selection_row(data, index):
    greatest_letter = data[get_position_of_highest(data, index)]
    swap_letter = data[index]

    data[index] = greatest_letter
    data[get_position_of_highest(data, index)] = swap_letter
    return

#q7
def my_selection_sort(data):
    for pass_num in range(len(data)-1, 0, -1):
        selection_row(data, pass_num)
    return

#q9
def shifting(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and data[i] > item_to_check:
        data[index] = data[i]
        index -=1
        i -= 1
    return

#q10
def insertion_row(data, index):	
    item_to_insert = data[index]
    i = index - 1
    while  i >= 0 and data[i] > item_to_insert:
        data[index] = data[i]
        index -=1
        i -= 1
    data[i + 1] = item_to_insert
    return

#q11
def my_insertion_sort(data):	
    for index in range(1, len(data)):
        insertion_row(data, index)
    return

#q12
def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_index = (max_index + min_index) // 2
        if numbers[mid_index] == value:
            return mid_index
        elif numbers[mid_index] < value:
            min_index = mid_index + 1
        elif numbers[mid_index] > value:
            max_index = mid_index - 1
    return -1

def main():
    numbers = [10, 15, 20, 27, 41, 69]
    print(binary_search(numbers, 69))
    numbers = [13, 18, 54, 61, 78, 93]
    print(binary_search(numbers, 54))
    return

main()
