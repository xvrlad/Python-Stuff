def sum_list_of_lists(numbers):
    total = 0
    result_list = [sum(lists) for lists in numbers]
    return result_list

def create_phonebook(lines):
    name_number_list = [strings.split(",") for strings in lines]
    name_number_list = [sublists[:2] for sublists in name_number_list]
    phonebook_dict = {name_number[0]:name_number[-1] for name_number in name_number_list}
    return phonebook_dict

def get_last_letter_dictionary(sentence):
    last_letter_dict = {}
    sentence = sentence.lower()
    list_of_strings = sentence.split()
    for word in list_of_strings:
        last_letter = word[-1]
        if (word and last_letter) not in last_letter_dict:
            last_letter_dict[last_letter] = [word]
        elif word not in (last_letter_dict and last_letter_dict[last_letter]):
            last_letter_dict[last_letter] += [word]
    return last_letter_dict

def main():
##    lines = ['Liam,45643454,liam@abc.com', 'Noah,43576413,noah.doe@gmail.com', 'Tony,56543239,tony@hr.mycompany.com', 'Bert,99275234,bert@support.com']
##    phonebook = create_phonebook(lines)
##    for name in sorted(phonebook.keys()):
##        print(name, phonebook[name])
    sentence = "May your coffee be strong and your Monday be short"
    abc_dictionary = get_last_letter_dictionary(sentence)
    for key in sorted(abc_dictionary.keys()):
            print(key, ' '.join(sorted(abc_dictionary[key])))
    return

main()
