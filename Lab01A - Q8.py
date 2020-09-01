star = "*"
space = " "
prompt = "Enter number of rows: "
number_of_rows = int(input(prompt))
mid_rows = (number_of_rows // 2) + 1

i = 4
print(star * number_of_rows)
for rows_in_between in range(mid_rows - 2):
    print(star + space * rows_in_between + star + space * (number_of_rows - i) + star + space * rows_in_between + star)
    i += 2
middle_row = star + space * (mid_rows - 2) + star + space * (mid_rows - 2) + star
print(middle_row)
i = 1
for rows_in_between in range(mid_rows - 3, -1, -1):
    print(star + space * rows_in_between + star + space * (i) + star + space * rows_in_between + star)
    i += 2
print(star * number_of_rows)
