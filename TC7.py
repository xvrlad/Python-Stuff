def get_biggest_two(numbers_tuple):
    if len(numbers_tuple) < 2:
        return numbers_tuple
    else:
        numbers_list = list(numbers_tuple)
        numbers_list.sort()
        largest_number = numbers_list[-1]
        second_largest_no = numbers_list[-2]
        new_tuple = (second_largest_no, largest_number)
    return new_tuple

def get_last_name_in_file(filename):
    read_file = open(filename, "r")
    contents = read_file.read()
    read_file.close()
    
    contents = contents.split(" ")
    new_list = []
    for elements in contents:
        if elements.isalpha():
            new_list.append(elements)
    final_name = new_list[-1] 
    return final_name

def main():
    numbers = (4, 7,   8,  1,   2,   5)
    print(get_biggest_two(numbers))

    print(get_biggest_two((23,)) )
    print()
    name = get_last_name_in_file("TimedExercise07Q02.txt")
    print(name)
    return

main()
