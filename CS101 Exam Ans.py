def list_equality(list1, list2):
    if len(list1) != len(list2):
        return False
    for elements in list1:
        if elements not in list2:
            return False
    for elements in list2:
        if elements not in list1:
            return False
    return True

def nested_loop_question(number):
    total = 0
    for i in range(1, number + 1):
        for j in range(i):
            total += 1
    return total

def main():
##    print(nested_loop_question(7))
##    print(nested_loop_question(13))
##    func([1,2,3], [0])
##    booleans1("abg", "ags", "g")
    booleans_3(30)
    booleans_3(51)
    booleans_3(53)
    booleans_3(59)
    a_list = [5,4]
    do_something_b(a_list)
    print(a_list)
    return

data_dict = {"Balrog" : [73, 67, 47, 44],
             "Bison" : [63, 54, 25],
             "Chun Li" : [95, 89, 72, 66],
             "Ken" : [100, 75, 65, 55], 
             "Ryu" : [100, 95, 80, 70]}

def func(list1, list2):
    """
    Doctest that evaluates the else branch (#1).
    >>> func([1, 2, 3], [1, 2, 3])
    num_list1.num_list2 = 14
    <BLANKLINE>
    ||num_list1 - num_list2|| = 0.0
    """
    if len(list1) != len(list2):
        print("Error!")
    else:
        calc1 = 0
        for i in range(len(list1)):
            calc1 += list1[i] * list2[i]
        calc2 = 0
        for i in range(len(list1)):
            calc2 += (list1[i] - list2[i]) ** 2
        calc2 = round(calc2 ** 0.5, 2)
        print("num_list1.num_list2 =", calc1)
        print()
        print("||num_list1 - num_list2|| =", calc2)
    
    return

##import doctest
##doctest.testmod()

def booleans1(word1, word2, letter):
##    exactly_divisible = len(str(number1)) == 3 and (number1 % number2 == 0 or number2 % number1 == 0)
##    if exactly_divisible:
##        print("yes")
    contains_letter = (letter in word1 and word2) and word1[0] != word2[0]
    if contains_letter:
        print("YES")
    return

def booleans_3(value):
    if value > 14 and value < 65 and value % 5 == 0 or value % 2 == 0:
        print("A")
    elif value % 3 == 0 or value % 2 == 0 and value > 42:
        print("B")
    elif value < 54:
        print("C")
    else:
        print("D")
    return

def do_something_b(list1):
    list2 = list1
    list1 = [4,3]
    for element in [1,5,3]:
        if element not in list1:
            list1.append(element)
    list1 = list2


main()
