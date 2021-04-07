class Contact:
    def __init__(self, name, phone_number, email, status=True):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__status = status

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def is_active(self):
        return self.__status

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_email(self, email):
        self.__email = email

    def set_active(self, value):
        self.__status = value

    def __str__(self):
        if self.__status:
            return_string = f"{self.__name} ({self.__phone_number}), {self.__email}"
        else:
            return_string = f"{self.__name} is an inactive record."
        return return_string

class PhoneBook:
    def __init__(self, phone_book=None):
        if phone_book == None:
            phone_book = []
        self.__phone_book = phone_book

    def load_records(self, filename):
        try:
            read_file = open(filename, 'r')
            file_contents = read_file.read()
            read_file.close()

            file_contents = file_contents.split()
            for element in file_contents:
                first_comma = element.find(",")
                second_comma = element.rfind(",")
                new_contact = Contact(element[:first_comma], element[first_comma + 1: second_comma],
                                      element[second_comma + 1:])
                self.__phone_book.append(new_contact)

            print(f"{len(self.__phone_book)} records loaded.")

        except FileNotFoundError:
            print(f"ERROR: The file '{filename}' does not exist.")

    def show_all_records(self):
        for contact_object in self.__phone_book:
            print(contact_object)

    def __len__(self):
        return len(self.__phone_book)

    def find_record(self, search_name):
        for contact_object in self.__phone_book:
            if contact_object.get_name() == search_name:
                return contact_object
        return None

    def update_phone(self, search_name, phone_number):
        for contact_object in self.__phone_book:
            if contact_object.get_name() == search_name:
                contact_object.set_phone_number(phone_number)
                print(f"{search_name}'s contact is updated.")
                return
        print(f"ERROR: {search_name} is not found.")

    def set_active(self, search_name):
        for contact_object in self.__phone_book:
            if contact_object.get_name() == search_name:
                contact_object.set_active(True)
                print(f"{search_name} is active from now on.")
                return
        print(f"ERROR: {search_name} is not found.")

    def set_inactive(self, search_name):
        for contact_object in self.__phone_book:
            if contact_object.get_name() == search_name:
                contact_object.set_active(False)
                print(f"{search_name} is inactive from now on.")
                return
        print(f"ERROR: {search_name} is not found.")

    def show_active_records(self):
        for contact_object in self.__phone_book:
            if contact_object.is_active():
                print(contact_object)

#Recursion section
def get_sum_ascii(word):
    if len(word) == 1:
        return ord(word)
    else:
        first_letter = ord(word[0])
        next_letter = get_sum_ascii(word[1:])
        return first_letter + next_letter

def get_sum_digits(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        previous_digit = get_sum_digits(number // 10)
        return last_digit + previous_digit

def get_min_odd(numbers):
    if len(numbers) == 1:
        return numbers[0] if numbers[0] % 2 != 0 else 9999
    else:
        first_number = numbers[0] if numbers[0] % 2 != 0 else 9999
        next_number = get_min_odd(numbers[1:])
        smallest_number = min(first_number, next_number)
        return smallest_number

def get_odds_list(numbers):
    if len(numbers) == 1:
        return [numbers[0]] if numbers[0] % 2 != 0 else []
    else:
        first_number = [numbers[0]] if numbers[0] % 2 != 0 else []
        next_number = get_odds_list(numbers[1:])
        return first_number + next_number

def get_merge_list(list_of_lists):
    if len(list_of_lists) == 1:
        return list_of_lists[0]
    else:
        first_list = list_of_lists[-len(list_of_lists)]
        next_list = get_merge_list(list_of_lists[1:])
        return first_list + next_list

#q10
def palindrome_filter(sentence):
    sentence = sentence.lower()
    if len(sentence) == 1:
        return sentence[0] if sentence[0].isalpha() else ""
    else:
        first_character = sentence[0] if sentence[0].isalpha() else ""
        next_character = palindrome_filter(sentence[1:])
        return first_character + next_character
#this part needs explanation as to why this works lmao, but you figured it out
def is_palindrome(sentence):
    if sentence == "":
        return True
    elif sentence[0] == sentence[-1]:
        return is_palindrome(sentence[1:-1])
    return False

#q11
def get_gcd(m,n):
    if max(m,n) % min(m,n) == 0:
        return min(m,n)
    else:
        return get_gcd(min(m,n), max(m,n)-min(m,n))




    # if reversed_sentence != sentence:
    #     return False
    # return True

    # print(sentence)
    # if len(sentence) == 0:
    #     return sentence
    # else:
    #     if sentence == "":
    #         return True
    #     # is_palindrome(sentence[1:-1])
    #     is_palindrome(sentence[1:len(sentence)])
    #     first_character = sentence[0]
    #     last_character = sentence[-1]
    #     if first_character != last_character:
    #         return False
    #     print(first_character, last_character)
    #     # is_palindrome(sentence[1:-1])
    #
    #     return True


def main():
    print(get_gcd(100, 70))
    print(get_gcd(2, 6))

    # print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))
    # print(is_palindrome(palindrome_filter("Ebla was I ere I saw Elba.")))
    # print(is_palindrome(""))
    # print(is_palindrome(palindrome_filter("Do geeses see God?")))

    # my_phonebook = PhoneBook()
    # my_phonebook.load_records("contacts.txt")
    # print("The phonebook contains {} contacts.".format(len(my_phonebook)))
    # my_phonebook.show_all_records()
    # #the phonebook object stays as an object throughout the creation of the code,
    # #must reset the object manually, thus the None in load_records
    # my_phonebook = PhoneBook()
    # my_phonebook.load_records('input_file.txt')
    # print("The phonebook contains {} contacts.".format(len(my_phonebook)))
    return

main()