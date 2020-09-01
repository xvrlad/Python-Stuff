"""
Author - Xavier Ladores
xlad198
Apr 4, 2020
Program that calculates ticket prices
"""
def main():
    request = "Enter number of tickets required: "
    tickets = get_number_from_user(request)
    full_price = get_ticket_price(tickets, 15)
    discount = get_discount(tickets, full_price)
    display_ticket_price(tickets, full_price, discount)
    
def display_ticket_price(tickets, price, discount):
    discounted_price = price - discount
    gst = get_gst_amount(discounted_price)
    print("*" * 20)
    print("Tickets:", tickets)
    print("Price: $", discounted_price, " (discount included: $",
          discount, ").", sep= "")
    print("GST included: $", gst, sep= "")
    print("*" * 20)
    return

def get_gst_amount(price):
    gst_amount = price * 0.15
    gst_amount = round(gst_amount, 2)
    return gst_amount

def get_discount(number_of_tickets, total_price):
    four_dollar_discount = 4 * number_of_tickets
    ten_percent_discount = 0.1 * total_price
    bigger_discount = max(four_dollar_discount, ten_percent_discount)
    bigger_discount = round(bigger_discount)
    return bigger_discount

def get_ticket_price(number_of_tickets, ticket_price):
    total = number_of_tickets * ticket_price
    rounded_total = round(total)
    return rounded_total

def get_number_from_user(prompt):
    integer_prompt = int(input(prompt))
    return integer_prompt

main()

