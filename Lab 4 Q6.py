"""
Lab 4:
"""

def main():
    result = test_number(33)
    print(result)
    print(test_number(28))
    print(test_number(30))

def test_number(value):
    if value < 30 or value > 50:
        return False
    if value % 2 == 0:
        return True
    else:
        return False
    return

main()








