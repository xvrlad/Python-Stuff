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

class MyLibrary:
    def __init__(self, ):

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

def main():
    m1 = Member(1001, "Michael")
    b1 = Book("QS12.03.001", "The Lord Of The Rings")
    b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
    b3 = Book("QS12.02.003", "The Dune Chronicles")
    r1 = Record(b1, m1, "2020-08-12")
    print(r1)
    r2 = Record(b3, m1, "2020-08-15")
    print(r2)
    r1.return_book()
    print()
    print(r1)
    print()
    print(b1)
    print()
    print(m1)
    print()
    m1 = Member(1001, "Michael")
    b1 = Book("QS12.03.001", "The Lord Of The Rings")
    b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
    b3 = Book("QS12.02.003", "The Dune Chronicles")
    r1 = Record(b1, m1, "2020-08-12")
    print(r1)
    r2 = Record(b3, m1, "2020-08-15")
    print(r2)
    r1.return_book()
    print()
    print(b1.is_available())
    return

main()