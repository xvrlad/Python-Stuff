#q1
def count_down(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        count_down(n-1)
    return

#q2
def copy_string(word):
    index = 0
    if len(word) == 1:
        character = word
        return character
    else:
        first_letter = word[index]
        next_letter = reverse_string(word[index + 1:])
        return first_letter + next_letter

#q3
def reverse_string(word):
    index = -1
    if len(word) == 1:
        character = word
        return character
    else:
        first_letter = word[index]
        next_letter = reverse_string(word[:index])
        return first_letter + next_letter

#q4
def print_between(start, end):
    if start == end:
        print(end)
    else:
        print(start, end= " ")
        print_between(start+1, end)
    return

#q5
def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    if len(word) == 1:
        return 1 if word in consonants else 0
    else:
        first_letter = 1 if word[0]  in consonants else 0
        rest = count_consonants(word[1:])
        return first_letter + rest

#q6
def get_first_lower_case(word):
    if len(word) == 0:
        return None
    elif word[0].islower():
        return word[0]
    else:
        first_letter = get_first_lower_case(word[1:])
        return first_letter

#q7
def get_max_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        maximum = get_max_list(numbers[1:])
    return max(numbers[0], maximum)

#q8
def get_max_len_list(words):
    if len(words) == 1:
        return len(words[0])
    else:
        maximum = get_max_len_list(words[1:])
        return max(len(words[0]), maximum)

#q9
def no_evens(numbers):
    if numbers[0] % 2 == 0:
        return False
    elif len(numbers) == 1 and numbers[0] % 2 != 0:
        return True
    else:
        check_evens = no_evens(numbers[1:])
        return check_evens

#q10
def evaluate_m(i):
    if i == 1:
        return 1/i
    else:
        sum = 1/i + evaluate_m(i-1)
        return sum

def main():
    print('{} : {}'.format(2, evaluate_m(2)))
    print('{} : {:.4}'.format(5, evaluate_m(5)))
    return

main()