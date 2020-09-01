prompt = "Enter a word: "
string = input(prompt)
letter_list = list(string)
letter_list.sort()

new_dict = {}
for letters in letter_list:
    if letters not in new_dict:
        new_dict[letters] = ord(letters)
for letters, asciis in new_dict.items():
    print("{}:{}".format(letters,asciis))
