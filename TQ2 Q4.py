prompt = "Enter number of rows: "
number_of_rows = int(input(prompt))
space = " "
star = "*"

top_row = print(space*(number_of_rows - 1) + star)
number_of_spaces = number_of_rows - 2
for spaces in range(number_of_spaces):
    print(space * number_of_spaces + star + space * spaces + star)
    number_of_spaces -= 1
bottom_row = print(star*number_of_rows)
