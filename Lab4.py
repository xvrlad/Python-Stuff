#q1
def is_valid_radius(radius):
    try:
        if radius > 0:
            return True
        else:
            raise "ERROR: Invalid radius!"
    except (TypeError, ValueError):
        return "ERROR: Invalid radius!"
    return
#q2
def is_valid_score(score):
    try:
        if 0 <= score <= 100:
            return True
        else:
            raise "ERROR: Invalid score!"
    except (TypeError, ValueError):
        return "ERROR: Invalid score!"
    return

#q3
def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvxyz"
    try:
        if word.isdigit() or word == "":
            return 0
        letter_list = list(word.lower())
        count = 0
        for letter in letter_list:
            if letter in consonants:
                count += 1
    except AttributeError:
        return "ERROR: Invalid input!"
    return count

#q4
def set_list_element(a_list, index, value):
    try:
        a_list[index] = value
    except IndexError:
        print("ERROR: Invalid index: {}.".format(index)) 
    except TypeError:
        print("ERROR: Invalid input.")
    return

#q5
def get_max(numbers):
    try:
        max_number = float(max(numbers))
    except (TypeError, ValueError):
        return "ERROR: Invalid number!"
    return max_number

#q6
def get_sum_even(numbers):
    the_sum = 0
    try:
        for elements in numbers:
            if type(elements) == int and elements % 2 == 0:
                the_sum += elements
    except:
        return
    return the_sum

#q7
def get_valid_input():
    number = -1 #default
    while not 1 <= number <= 10:
        user_input = input("Enter a number between 1 and 10 inclusive: ")
        try:
            number = float(user_input)
        except ValueError:
            pass
    return number

#q8
def get_volume(radius, height):
    import math
    try:
        volume = round(math.pi * radius**2 * height)
        if radius < 0 or height < 0 or (radius < 0 and height < 0) or (radius == 0 or height == 0):
            raise ValueError()
    except ValueError:
        if radius < 0 and height < 0:
            return "ERROR: Height and radius must be positive."
        elif radius < 0:
            return "ERROR: Radius must be positive."
        elif height < 0:
            return "ERROR: Height must be positive."
        elif radius == 0 or height == 0:
            return "ERROR: Not a cylinder."
    except TypeError:
        return "ERROR: Invalid input."
    return volume

#q9
def get_maori_word(dictionary, word):
    try:
        return dictionary[word]
    except KeyError:
        return "ERROR: {} is not available.".format(word)
    return

#q10
def get_phone(phones_dictionary, name):
    try:
        if type(name) != str or name == "":
            raise TypeError
        return phones_dictionary[name]
    except TypeError:
        if type(name) != str:
            return "ERROR: Invalid input!"
        elif name == "":
            return "ERROR: Invalid name!"
    except KeyError:
        return "ERROR: {} is not available.".format(name)
    return

#q11
def read_scores(filename):
    try:
        if type(filename) != str or filename == "":
            raise TypeError()
        input_file = open(filename, "r")
        scores = input_file.read().split()
        numbers = [float(score) for score in scores if float(score) >= 0 ]
        input_file.close()

        number_of_marks = len(numbers)
        if number_of_marks == 0:
            raise TypeError()
        total_marks = sum(numbers)
        print("There are {} score(s).".format(number_of_marks))
        print("The total is {:.2f}.".format(total_marks))
        print("The average is {:.2f}.".format(total_marks/number_of_marks))
    except ValueError:
        print("ERROR: The input file contains invalid values.")
    except TypeError:
        if type(filename) != str:
            print("ERROR: Invalid input!")
        elif filename == "":
            print("ERROR: Invalid filename!")
        elif number_of_marks == 0:
            print("ERROR: No positive scores in the input file.")
    except FileNotFoundError:
        print("ERROR: The file '{}' does not exist.".format(filename))
    return

def main():
    print("Valid input: {}".format(get_valid_input()))
    return


main()
