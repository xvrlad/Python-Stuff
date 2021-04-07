def foo(number):
    word = str(number % 4)
    if number % 4 == 0:
        return word
    else:
        return foo(number // 4) + word

def main():
    print(foo(13))
    return

main()