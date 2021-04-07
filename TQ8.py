def get_folding_hash(key, table_size):
    key = str(key)
    pair_list = []
    i = 0
    next_index = i + 1
    while next_index < len(key):
        pair_list.append(int(key[i] + key[next_index]))
        i += 2
        next_index += 2
    if len(key) % 2 != 0:
        pair_list.append(int(key[next_index - 1]))
    return sum(pair_list) % table_size

def hash_string(key, table_size):
    sum = 0
    for pos in range(len(key)):
        sum = sum + ord(key[pos])
    return sum % table_size

def get_weighted_hash(key, table_size):
    if len(key) == 1:
        return ord(key)
    sum = ord(key[0]) + get_weighted_hash(key[1:], table_size)
    return sum


class Student:
    def __init__(self, first_name, surname, student_id, email_address):
        self.__first_name = first_name
        self.__surname = surname
        self.__student_id = student_id
        self.__email_address = email_address
        self.__test_mark = 0
        self.__exam_mark = 0
        self.__lab_marks = []

    def __str__(self):
        return '{}, {}: id={} ({})'.format(self.__surname.title(), self.__first_name.title(), self.__student_id,
                                           self.__email_address)

    def __eq__(self, other):
        if self.__student_id == other.__student_id:
            return True
        return False

    def __hash__(self):
        return get_simple_hash(self.__student_id, 11)

def main():
    # print(get_weighted_hash('cat', 13))
    # print(get_weighted_hash('dog', 13))
    #
    # print(get_weighted_hash('dog', 13))
    # print(get_weighted_hash('god', 13))
    print(get_folding_hash(1234, 7))
    print(get_folding_hash(12345, 11))
    return


main()
