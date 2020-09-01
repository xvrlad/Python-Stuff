"""
Lab 4:
"""

def main():
    print_even_numbers(6, 20)
    print()

    print_even_numbers(7, 20)
    print()

    print_even_numbers(-9, 5)
    print()

    print_even_numbers(21, 4)

    print_even_numbers(-14, -14)

    print_even_numbers(-13, -13)

def print_even_numbers(first_num, last_num):
    if last_num < first_num:
        return
    if first_num == last_num and first_num % 2 != 0:
        return
    if first_num == last_num and first_num % 2 == 0:
        print(first_num)
        return
    elif first_num % 2 == 0:
        print(first_num, end= " ")
        while first_num < last_num:
            first_num = first_num + 2
            print(first_num, end= " ")
    else:
        first_num = first_num + 1
        print(first_num, end= " ")
        while first_num < (last_num - 1):
            first_num = first_num + 2
            print(first_num, end= " ")
    return
        
        

main()








