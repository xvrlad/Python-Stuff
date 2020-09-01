"""
Lab 3: Program 2 (Question 6)
Author - Xavier Ladores
xlad198
Apr 4, 2020
Program that
"""

def main():
    print("1.", get_first_last_number(74678))
    print("2.", get_first_last_number(-455))
    print("3.", get_first_last_number(1437))
    print("4.", get_first_last_number(0))

def get_first_last_number(number):
    absolute_value = abs(number)
    string_conversion = str(absolute_value)
    first_number = string_conversion[0]
    last_number = string_conversion[-1]
    first_last_number = first_number + last_number
    first_last_number = int(first_last_number)
    return first_last_number
    
main()








