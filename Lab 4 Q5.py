"""
Lab 4:
"""

def main():
    letter = get_letter("Dreams")
    print(letter)

    print(get_letter("programming"))

def get_letter(word):
    print(word)
    prompt = int(input("Enter index: "))
    while prompt < 0 or prompt >= len(word):
        prompt = int(input("Enter index: "))
    else:
        character = word[prompt]
    return character

main()








