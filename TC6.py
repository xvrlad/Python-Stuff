def change_negatives_to_zero(numbers_list):
    i = 0
    while i < len(numbers_list):     
        for numbers in numbers_list:
            if numbers < 0:
                numbers_list.pop(i)
                numbers = 0
                numbers_list.insert(i, numbers)
            i = i + 1
    return numbers_list

def remove_3_digit_numbers(numbers_list):
    for numbers in range(len(numbers_list) - 1, -1 , -1):
        number = numbers_list[numbers]
        if number >= 100 and number < 1000:
            numbers_list.pop(numbers)
    return


def main():
    numbers_list = [117, -241, -171, 112, 317, 290, 77, 394]
    change_negatives_to_zero(numbers_list)
    print(numbers_list)

    numbers_list = [117, 41, 171, 112, 317, 290, 77, 39]
    remove_3_digit_numbers(numbers_list)
    print(numbers_list)
    return

main()
