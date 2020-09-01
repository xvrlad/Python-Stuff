prompt = "Enter a sentence: "
sentence = input(prompt)
sentence = sentence.lower()
sentence_list = sentence.split()

new_dict = {}
new_list = []

for words in sentence_list:
    length = len(words)
    if length in new_dict and (words not in new_dict[length]):
        new_dict[length] = new_dict[length] + [words]
    else:
        new_dict[length] = [words]

for keys, values in new_dict.items():
    if keys not in new_list:
        new_list.append(keys)
        new_list.sort()

for address in new_list:
    print(address, end= " ")
    word_list = new_dict[address]
    word_list.sort()
    for words in word_list:
        print(words, end= " ")
    print()
    
