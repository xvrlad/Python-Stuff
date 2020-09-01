#q9
def append_to(element, values=None):
    if values == None:
        values = []
    values.append(element)
    return values

#q10
def print_values(dictionary):
    key_list = list(dictionary.keys())
    key_list.sort()
    for key in key_list: 
        print(dictionary[key], end=" ")

#q11
def word_len_frequencies(sentence):
    dict1 = {}
    dict2 = {}
    sentence = sentence.lower()
    word_list = sentence.split()
    for word in word_list:
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
    for key in dict1:
        value = dict1[key]
        if value not in dict2:
            dict2[value] = [key]
        else:
            dict2[value].append(key)
        dict2[value].sort()
    key_list = list(dict2.keys())
    key_list.sort()
    key_list.reverse()
    for key in key_list:
        line = str(key) + ' ' + str(dict2[key])
        print(line)
    
def main():
    word_len_frequencies('the Quick BROWN fox jumps fox fox fox quick')
    print()
    word_len_frequencies('this is a really long sentence of words and there will be some repeated words in this really long sentence of words')
    return

main()
