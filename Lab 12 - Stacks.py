#Stack Implementation
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items == []:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items.pop()

    def peek(self):
        if self.__items == []:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items[len(self.__items) - 1]

    def __str__(self):
        return f"Stack: {self.__items}"

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def push_list(self, a_list):
        self.__items += a_list

    def multi_pop(self, number):
        if number <= self.__len__():
            for pops in range(number):
                self.pop()
            return True
        return False

    def copy(self):
        stack_copy = Stack() #you can instantiate the class within itself like this
        stack_copy.push_list(self.__items)
        return stack_copy

    def __eq__(self, other):
        if type(other) != Stack: #the type is Stack
            return False
        elif self.__items == other.__items:
            return True
        return False

#Stack Application
def reverse_sentence(sentence):
    new_stack = Stack()
    word_list = sentence.split()
    for word in word_list:
        new_stack.push(word)
    new_string = ''
    for pops in range(new_stack.size()):
        new_string += new_stack.pop() + " "
    return new_string

def is_balanced_brackets(text):
    new_stack = Stack()
    for iteration in range(len(text)):
        character = text[iteration]
        if character == '}' or character == ']' or character == ')':
            if new_stack.size() == 0:
                return False
            check_bracket = new_stack.pop()
            if check_bracket + character not in "(){}[]":
                return False
        elif character == '{' or character == '[' or character == '(':
            new_stack.push(character)
    if new_stack.size() != 0:
        return False
    return True
#q10
def evaluate_postfix(postfix_list):
    new_stack = Stack()
    for element in postfix_list:
        if element.isdigit():
            new_stack.push(element)
        else:
            last_operand = int(new_stack.pop())
            first_operand = int(new_stack.pop())
            new_stack.push(compute(first_operand, last_operand, element))
    return new_stack.pop()

def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 // number2
    elif operator == '^':
        return number1 ** number2
    else:
        return number1 % number2

def main():
    # #q9
    # postfix_stack = Stack()
    # postfix_stack.push(3)
    # postfix_stack.push(4)
    # four = postfix_stack.pop()
    # three = postfix_stack.pop()
    # postfix_stack.push(four * three)
    # postfix_stack.push(6)
    # six = postfix_stack.pop()
    # twelve = postfix_stack.pop()
    # postfix_stack.push(12 / 6)
    # postfix_stack.push(3)
    # three = postfix_stack.pop()
    # two = postfix_stack.pop()
    # print(three+two)

    # s1 = Stack()
    # for i in range(4, 7):
    #     s1.push(i)
    # s2 = Stack()
    # for i in range(4, 7):
    #     s2.push(i)
    # s2.push('aaskdhlakjh')
    # print(s1 == s2)
    # print(s1)
    # print(s2)
    #
    # s1 = Stack()
    # for i in range(4, 7):
    #     s1.push(i)
    # a_list = [4, 5, 6]
    # print(s1 == a_list)
    # print(s1)
    # print(a_list)

    # try:
    #     s = Stack()
    #     print(s.pop())
    # except IndexError as err:
    #     print(err) #err is a variable that is passed an object (like a str)
    #                #attached to the exception class (in this case IndexError).
    #
    # try:
    #     s = Stack()
    #     print(s.peek())
    # except IndexError as err:
    #     print(err)
    # return

main()