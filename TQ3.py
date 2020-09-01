#q1
def has_two_adjacent(numbers):
    for index in range(len(numbers) - 1):
        if numbers[index] == numbers[index+1]:
            return True
    return False

#q2
def get_pair_of_largest_numbers(numbers):
    result = [numbers[index] + numbers[index+1] for index in range(len(numbers)-1)]
    max_value = result[0]
    for index in range(len(result)):
        if result[index] > max_value:
            max_value = result[index]
        new_tuple = numbers[index], numbers[index+1]
    return new_tuple

#q3
def read_numbers(filename):
    try:
        if type(filename) != str:
            raise TypeError
        result = []
        input_file = open(filename, "r")
        content = input_file.readlines()
        input_file.close()
        for line in content:
            words = line.split()
            numbers = []
            for word in words:
                try:
                    number = float(word)
                except ValueError:
                    pass
                else:
                    numbers.append(number)
            total_marks = sum(numbers)
            result.append(total_marks)
        print(result)
    except TypeError:
        print("ERROR: Invalid parameter: filename needs to be a string!")
    except FileNotFoundError:
        print("ERROR: The file '{}' does not exist.".format(filename))
    return

def main():
    read_numbers("eight_numbers.txt")
    read_numbers('input_unknown.txt')
    read_numbers('empty.txt')
    read_numbers(123)
    read_numbers("with_invalid.txt")
    return

main()

