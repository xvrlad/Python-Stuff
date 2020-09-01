def get_change(items, price_per_item, amount_tendered):
    cost_of_items = items * price_per_item
    change = abs(cost_of_items - amount_tendered)
    change = round(change, 2)
    return change

def get_inner_number(number):
    integer = str(number)
    if len(integer) < 3:
        inner_number = int("0")
    else:
        if number < 0:
            positive_conversion = abs(number)
            positive_string = str(positive_conversion)
            inner_number = int(positive_string[1:-1])
        else:
            inner_number = int(integer[1:-1])
    return inner_number

print(get_inner_number(-39478))
print(get_inner_number(4))        
print(get_inner_number(39845) + 10)
