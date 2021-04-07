def get_sum_string_lengths(words):
    if len(words) == 0:
        return len(words)
    else:
        return len(words[0]) + get_sum_string_lengths(words[1:])

def evaluate_f(number):
    if number == 1:
        return 0
    else:
        return evaluate_f(number - 1)

def decimal_to_binary(number):
    pass

def main():
    val = evaluate_f(3)
    print(val)
    val = evaluate_f(8)
    print(val)
    val = evaluate_f(1)
    print(val)
    val = evaluate_f(2)
    print(val)
    return

main()