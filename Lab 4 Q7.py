"""
Lab 4:
"""

def main():
    result = test_string("Antonid")
    print(result)
    print(test_string("Anatonis"))
    print(test_string("PD"))

def test_string(phrase):
    vowels = "aeiou"
    uppercase_vowels = "AEIOU"

    first_letter = phrase[0]
    last_letter = phrase[-1]

    first_letter_vowel_index = vowels.find(first_letter)
    last_letter_vowel_index = vowels.find(last_letter)

    first_letter_vowel_index_uppercase = uppercase_vowels.find(first_letter)
    last_letter_vowel_index_uppercase = uppercase_vowels.find(last_letter)

    if len(phrase) % 2 != 0:
        return False
    if first_letter_vowel_index > -1 or last_letter_vowel_index > -1 or first_letter_vowel_index_uppercase > -1 or last_letter_vowel_index_uppercase > -1:
        return True
    else:
        return False
    return
    

main()








