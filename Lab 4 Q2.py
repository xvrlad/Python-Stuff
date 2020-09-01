"""
Lab 4:
"""

def main():
    price = get_ticket_price(5, 20, True, False)
    print("$" + str(price))
    print("$" + str(get_ticket_price(5, 20, False, True)))
    print("$" + str(get_ticket_price(5, 20, False, False)))
    print("$" + str(get_ticket_price(15, 25, False, True)))

def get_ticket_price(number_of_tickets, ticket_price, has_discount, is_a_member):
    total_price = number_of_tickets * ticket_price
    if has_discount and is_a_member:
        end_price = round(0.8 * total_price)
        return end_price
    elif has_discount:
        end_price = round(0.85 * total_price)
        return end_price
    elif is_a_member:
        end_price = round(0.9 * total_price)
        return end_price
    else:
        return total_price
    return

main()








