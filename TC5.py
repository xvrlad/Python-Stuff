def get_o_words_count(word_list):
    count = 0
    for words in word_list:
        little_o = "o"
        big_o = "O"
        if little_o in words or big_o in words:
            count = count + 1
    return count

def get_shortened_words(word_list):
    new_list = []
    for words in word_list:
        if len(words) > 2:
            letter1 = words[0]
            last_letter = words[-1]
            new_word = letter1 + last_letter
            new_list.append(new_word)
    return new_list

def main():
    word_list = ['hard', 'substitute', 'is', 'for', 'work', 'There', 'NO']
    print(get_o_words_count(word_list))
    print(get_o_words_count(['OUT', 'water', 'of', 'FISH']))
    print()
    word_list = ['you', 'it', 'do', 'do', 'whatever', 'well']
    short_words = get_shortened_words(word_list)
    print(short_words)
    print(get_shortened_words(['fish', 'out', 'of', 'water']))

main()
