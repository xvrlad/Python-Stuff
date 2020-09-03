class Book:
    def __init__(self, code, title, status=True):
        self.__code = code
        self.__title = title
        self.__status = status

    def get_book_title(self):
        return self.__title

    def get_book_code(self):
        return self.__code

    def is_available(self):
        return self.__status

    def borrow_book(self):
        self.__status = False

    def return_book(self):
        self.__status = True

    def __str__(self):
        if self.__status == False:
            string = "(On Loan)"
        else:
            string = "(Available)"
        return str(self.__title) + ", " + str(self.__code) + " " + string

class Member:
    def __init__(self, member_id, name, on_loan_books_list= []):
        self.__member_id = member_id
        self.__name = name
        self.__on_loan_books_list = on_loan_books_list

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list

    def borrow_book(self, book):
        self.__on_loan_books_list = self.__on_loan_books_list + [book.get_book_title()]

    def return_book(self, book):
        index = self.__on_loan_books_list.index(book.get_book_title())
        self.__on_loan_books_list.pop(index)

    def __str__(self):
        print(str(self.__name))
        print("On loan book(s):")
        if self.__on_loan_books_list == []:
            return "-"
        else:
            return "\n".join(self.__on_loan_books_list)

class Record:
    def __init__(self, book, member, issue_date):
        book.borrow_book()
        member.borrow_book(book)
        self.__book = book
        self.__member = member
        self.__is_on_loan = True
        self.__issue_date = issue_date

    def get_member_id(self):
        return self.__member.get_member_id()

    def get_book_code(self):
        return self.__book.get_book_code()

    def get_issue_date(self):
        return self.__issue_date

    def is_on_loan(self):
        if self.__book.is_available() == True:
            return False
        else:
            return True

    def return_book(self):
        self.__book.return_book()
        self.__member.return_book(self.__book)

    def __str__(self):
        return str(self.__member.get_name()) + ", " + str(self.__book) + ", issued date=" + str(self.__issue_date)

class MyLibrary:
    def __init__(self, filename):
        try:
            read_file = open(filename, 'r')
            contents = read_file.read()
            read_file.close()

            contents = contents.split("\n")
            books_list = []
            for elements in contents:
                comma_index = elements.index(",")
                code = elements[:comma_index]
                title = elements[comma_index + 1:]
                book_object = Book(code,title)
                books_list.append(book_object)
            # books_list = read_file.read()
            # read_file.close()
            #
            self.__books_list = books_list
            self.__on_loan_records_list = []

            print("{} books loaded.".format(len(self.__books_list)))
        except FileNotFoundError:
            print("ERROR: The file '{}' does not exist.".format(filename))
            self.__books_list = []

    def show_all_books(self):
        for book_object in self.__books_list:
            print(book_object)

    # def find_book(self, code):
    #     if code.isdigit():
    #         return None
    #     else:
    #         for book_object in self.__books_list:
    #             if code in book_object and book_object.isavailable():
    #                 print(book_object)
    #
    # def borrow_book(self, book, member, issue_date):
    #     if book == None:
    #         print("ERROR: could not issue the book.")
    #     else:
    #         new_record = Record(book, member, issue_date)
    #         self.__on_loan_records_list.append(new_record)
    #         print("The {} is borrowed by {}.".format(book, member))
    #
    #
    # def show_available_books(self):
    #     pass

def main():
    library = MyLibrary('simple_books.txt')
    print()
    library.show_all_books()
    print()
    library = MyLibrary('input_file.txt')
    library.show_all_books()
    # library = MyLibrary('simple_books.txt')
    # print()
    # b1 = library.find_book('003')
    # m1 = Member(1001, "Michael")
    # library.borrow_book(b1, m1, "2020-08-12")
    # print()
    # print(m1)
    # print()
    # library = MyLibrary('simple_books.txt')
    # print()
    # b1 = library.find_book('QS12.02.003')
    # m1 = Member(1001, "Michael")
    # library.borrow_book(b1, m1, "2020-08-12")
    # print()
    # b2 = library.find_book('QA12.04.004')
    # library.borrow_book(b2, m1, "2020-08-12")
    # print()
    # library.show_available_books()
    # print()
    # print(m1)
    return

main()