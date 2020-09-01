def main():
    print_right_angle_traingles('*', '-', 5)
    print()
    print_right_angle_traingles("$",'-', 3)
    print()

    print_hollow_square('#', 8)
    print()
    print_hollow_square("$", 3)
    print()
    return

def print_right_angle_traingles(symbol1, symbol2, number_of_rows):
    initial = 0
    for rows in range(number_of_rows - 1):
        for columns in range(number_of_rows):
            if columns < number_of_rows - initial - 1:
                print(symbol1, end= "")
            else:
                print(symbol2, end= "")
        print()
        initial += 1
    return

def print_hollow_square(symbols, number_of_rows):
    space = " "
    for rows in range(number_of_rows):
        for columns in range(number_of_rows):
            if rows == 0:
                print(symbols, end= "")
            elif 0 < rows < number_of_rows - 1:
                if columns == 0 or columns == number_of_rows - 1:
                    print(symbols, end= "")
                else:
                    print(space, end= "")
            elif rows == number_of_rows - 1:
                print(symbols, end= "")
        print()
    return

main()
