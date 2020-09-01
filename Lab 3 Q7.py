"""
Lab 3: Program 3 (Question 7)
Author: Xavier Ladores
xlad198
Apr 4, 2020
Program that
"""

def main():
    request = "Enter number (5 - 20): "
    handling_cost = 5
    cost_per_item = 4.25
    number_from_user = get_number(request)
    final_cost = get_cost(number_from_user, cost_per_item, handling_cost)
    cost_details = display_details(number_from_user, cost_per_item,
                                   handling_cost, final_cost)
	    
def get_number(prompt):
    return int(input(prompt))

def get_cost(number, cost_per_unit, handling_cost):
    total_cost = number * cost_per_unit + handling_cost
    return round(total_cost)

def display_details(items, cost_each, handling_cost, final_price):
    print()
    print("Items: ", items, " Cost per item: $", cost_each, sep="")
    print("Handling cost: $", handling_cost, sep="")
    print("Total: $", final_price, sep="")

main()








