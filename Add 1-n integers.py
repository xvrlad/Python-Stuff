"""
Program that adds consecutive numbers from 1 to x.
BY XAVIER LADORES
April 6, 2020 - August 14, 2020

Reason for making the program? Just because I thought it would be fun.
"""
#the function that actually does the calculations.
def number_adder(endpoint):
    start = 1
    next_number = start + 1
    initial = 1
    while initial < endpoint:
        start = start + next_number
        initial = initial + 1
        next_number = next_number + 1
    print("1 to", endpoint, "added consecutively is:", start)
    return

#the function that makes the program interactive.
def number_adder_interactive():
    prompt = ''
    while not prompt.isdigit():
        prompt = input(
            "Please enter an integer you wish to consecutively add up to: ")
        print()
        try:
            number_adder(int(prompt))
        except ValueError:
            print("Sorry, that was an invalid input, please try again.\n")
            pass
            
    print()
    quit_function()
    return

#as the name says, this function asks the user if they want to quit the program.
def quit_function():
    quit_prompt = input("Would you like to quit? Y/N: ")
    yes = "y"
    no = "n"

    while (quit_prompt != no) or (quit_prompt != yes):
        quit_prompt = quit_prompt.lower()
        if quit_prompt == no:
            print()
            number_adder_interactive()
            return
        elif quit_prompt == yes:
            print()
            return
        print("Sorry, you have entered an invalid input. Please try again.")
        quit_prompt = input("Quit? Y/N: ")
    return

#asks the user for their name.
def username_prompter(username):
    while len(username) > 30:
        print(
            "I'm sorry, your name is too long to process. Can you shorten it by any chance?")
        username = input("Please enter your shorter name: ")
    username_banner(username)
    number_adder_interactive()
    goodbye_banner(username)
    return

#creates a menu.
def username_banner(username):
    menu_string = "WELCOME, "
    extra_stars = 20
    print()
    print("=" * (extra_stars + len(menu_string) + len(username) + extra_stars))
    print(" " * extra_stars, menu_string, username,  sep= "")
    print("=" * (extra_stars + len(menu_string) + len(username) + extra_stars))
    print("THIS PROGRAM ADDS CONSECUTIVE INTEGERS FROM 1 TO n,",
          "WHERE n IS A GIVEN INTEGER.")
    return

#creates a goodbye menu.
def goodbye_banner(username):
    print("=" * 5, "Goodbye, {}. Thank you for trying out this program!".format(username), "=" * 5)
    return

#the main function where everything is executed from.
def main():
    username = input("Please enter your name: ")
    username_prompter(username)
    return

main()
