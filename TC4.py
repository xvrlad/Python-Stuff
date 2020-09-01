##def get_price(number_of_items, price_per_item):
##    if number_of_items <= 5:
##        final_price = round(number_of_items * price_per_item)
##        return final_price
##    elif number_of_items > 6 and number_of_items < 9:
##        final_price = number_of_items * price_per_item
##        discount = 0.1
##        discounted_price = round(final_price - (final_price * discount))
##        return discounted_price
##    elif number_of_items >= 10:
##        final_price = number_of_items * price_per_item
##        discount = 0.2
##        discounted_price = round(final_price - (final_price * discount))
##        return discounted_price
##    return

def remove_digit_nine(number_str):
    nine = number_str.find("9")

    while nine > -1:
        string_cut = number_str[:nine]
        number_str = number_str[nine + 1:]
        nine = number_str.find("9")
        print(string_cut, end= "")
    if nine == -1:
        string_cut_end = number_str[:nine]
        return string_cut_end
    return 

##
##        space_finder = phrase.find(" ")
##    last_character = phrase[-1]
##    while space_finder > -1:
##        string_part = phrase[:space_finder]
##        phrase = phrase[space_finder + 1:]
##        space_finder = phrase.find(" ")
##        print(string_part, end= "")
##    if space_finder == -1:
##        string_part_end = phrase[:space_finder]
##        print(string_part_end, end= "")
##    return last_character
        
print(remove_digit_nine('-3459'))
print(remove_digit_nine('23994596'))
print(remove_digit_nine('-99000'))
print(remove_digit_nine('94'))
print(remove_digit_nine('-9345'))
