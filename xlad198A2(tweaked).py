"""
Game of Ventuno
Author: Xavier Ladores
xlad198
Apr 22, 2020
"""

import random

def main():
    username = "xlad198" #change this to your username
    game_of_ventuno = "WELCOME TO THE GAME OF VENTUNO"
    print("=" * len(game_of_ventuno))
    print(game_of_ventuno)
    print("=" * len(game_of_ventuno))
    instruction()
    print()
    print("=" * len(game_of_ventuno))
    player_name = input("What is your name, player? ") #change this name
    option_new_game = 1
    option_see_stats = 2
    option_quit = 0

    number_of_games = 0
    won_by_user = 0
    won_by_computer = 0

    display_introduction('   ', username, player_name)
    selection = option_new_game

    while selection !=  option_quit:
        selection = get_main_menu_selection(" " * 5)

        if selection == option_new_game:
            number_of_games += 1
            winner_name = play_a_game(player_name)

            if winner_name == player_name:
                won_by_user += 1
            elif winner_name == "Computer":
                won_by_computer += 1

        elif selection == option_see_stats:
            display_statistics(player_name, number_of_games, won_by_user, won_by_computer)

    display_statistics(player_name, number_of_games, won_by_user, won_by_computer)
    print()
    print("Thank You For Playing Ventuno, " + player_name + "!")
    print()
#--------------------------------------------------------------
#--------------------------------------------------------------
# DO NOT CHANGE THE CODE ABOVE THIS LINE EXCEPT FOR THE FIRST LINE
#--------------------------------------------------------------
def instruction():
    print()
    print("The object of the game of Ventuno is to reach a score (by throwing a dice)")
    print("which is higher than the other player's score, but without going over 21.")
    print()
    print('If you go over 21, you "bust" and automatically lose the game.')
    print()
    print("When having a turn, the player can choose to either roll the dice and add that")
    print('score to their current score or the player can choose to "stay" at their current')
    print("score and in this case their score will not change for the rest of the game.")
    return
#--------------------------------------------------------------
# FOUR STAGE 1 FUNCTIONS
#--------------------------------------------------------------
#--------------------------------------------------------------
def display_line_of_symbols(indent, symbol, how_many):
    number_of_symbols = symbol * how_many
    print(indent + number_of_symbols)
    return

def display_introduction(indent, username, name):
    print()
    display_line_of_symbols(indent, "=", 27)
    print(indent + "Ventuno written by " + username)
    print(indent + "Welcome, " + name)
    display_line_of_symbols(indent, "=", 27)
    print()

def get_play_menu_selection(indent):
    print(indent + "")
    print(indent + "1. ROLL")
    print(indent + "2. STAY")
    print(indent + " " * 3, end= "")
    play_selection_prompt = int(input("Enter selection: "))
    return play_selection_prompt

def get_main_menu_selection(indent):
    print(indent + "")
    print(indent + "1. PLAY A NEW GAME")
    print(indent + "2. SEE STATS")
    print(indent + "0. QUIT")
    print(indent + " " * 3, end= "")
    menu_selection_prompt = int(input("Enter selection: "))
    return menu_selection_prompt

#--------------------------------------------------------------
#--------------------------------------------------------------
# FIVE STAGE 2 FUNCTIONS
#--------------------------------------------------------------
#--------------------------------------------------------------
def display_current_player(current_player):
    print(current_player + "'s turn:")
    return

def get_next_player(current_player, player_name):
    computer = "Computer"
    if len(current_player) == len(computer):
        initial = 0
        first_letter_current_player = current_player[initial]
        find_in_computer = computer.find(first_letter_current_player)
        while find_in_computer != -1 and initial < 7:
            initial = initial + 1
            first_letter_current_player = current_player[initial]
            find_in_computer = computer.find(first_letter_current_player)
        if initial < 7:
            return computer
        else:
            return player_name      
    else:
        return computer

def get_random_starting_player_name(player_name):
    random_number = random.randrange(1, 3)
    computer = "Computer"
    if random_number == 1:
        return player_name
    else:
        return computer

def add_dice_roll(current_score, current_player):
    random_die_value = random.randrange(1, 7)
    print(current_player, "'s dice roll: ", random_die_value, sep= "")
    the_sums = current_score + random_die_value
    return the_sums

def get_starting_score():
    random_number = random.randrange(12, 17)
    return random_number

#--------------------------------------------------------------
#--------------------------------------------------------------
# FIVE STAGE 3 FUNCTIONS
#--------------------------------------------------------------
#--------------------------------------------------------------
def display_current_scores(indent, score_player, score_computer, player_stays, computer_stays, player_name):
    print()
    display_line_of_symbols(indent, "-", 37)
    display_line_of_symbols(indent, "-", 37)
    if player_stays:
        print(indent + player_name + "'s score: " + str(score_player) + " - " + player_name + " stays")
    else:
        print(indent + player_name + "'s score: " + str(score_player))
    if computer_stays:
        print(indent + "Computer's score: " + str(score_computer) + " - Computer stays")
    else:
        print(indent + "Computer's score: " + str(score_computer))
    display_line_of_symbols(indent, "-", 37)
    display_line_of_symbols(indent, "-", 37)
    print()

def game_is_over(score_player, score_computer, player_stays, computer_stays):
    if score_player > 21 or score_computer > 21:
        return True
    elif player_stays and computer_stays:
        return True
    else:
        return False

def get_winner_name(score_player, score_computer, player_name):
    if score_player == score_computer:
        draw = "draw"
        return draw
    elif score_player > 21:
        computer = "Computer"
        return computer
    elif score_computer > 21:
        return player_name
    elif score_computer > score_player:
        return "Computer"
    else:
        return player_name
    

def display_game_result(indent, score_player, score_computer, game_winner, player_name):
    print()
    display_line_of_symbols(indent, "+", 25)
    display_line_of_symbols(indent, "+", 25)
    print()
    print(indent + player_name + "'s score: " + str(score_player))
    print(indent + "Computer's score: " + str(score_computer))
    print()

    computer_wins = game_winner.find("Computer")
    player_wins = game_winner.find(player_name)
    draw = game_winner.find("draw")
    if computer_wins == 0:
        print(indent + "HAHA, YOU LOSE!")
    elif player_wins == 0:
        print(indent + player_name + " YOU WON. GOOD FOR YOU...")
    elif draw == 0:
        print(indent + "IT'S A DRAW. BOOOORING!")
    print()
    display_line_of_symbols(indent, "+", 25)
    display_line_of_symbols(indent, "+", 25)
    return

def display_statistics(player_name, total_number_of_games, games_won_by_user, games_won_by_computer):
    print()
    print("*" * 32)
    print("*" * 32)
    print("  Number of games played: " + str(total_number_of_games))
    print("  Games won by " + player_name + ": " + str(games_won_by_user))
    print("  Games won by Computer: " + str(games_won_by_computer))
    games_that_were_a_draw = total_number_of_games - games_won_by_user - games_won_by_computer
    print("  Games resulting in a draw: " + str(games_that_were_a_draw))
    print()
    difference_of_scores = abs(games_won_by_user - games_won_by_computer)
    if games_won_by_user > games_won_by_computer:
        print("*** " + player_name + " is winning by " + str(difference_of_scores) + " *** ")
    elif games_won_by_computer > games_won_by_user:
        print("*** Computer is winning by " + str(difference_of_scores) + " *** ")
    elif difference_of_scores == 0:
        print("*** Final result is a draw ***")
    print("*" * 32)
    print("*" * 32)
    return

#--------------------------------------------------------------
#--------------------------------------------------------------
# ONE STAGE 4 FUNCTION
#--------------------------------------------------------------
#--------------------------------------------------------------
def get_computer_selection(score_player, score_computer, player_stays):
    roll = 1
    stay = 2
    ventuno = 21
    if score_player > score_computer and score_player <= ventuno:
        return roll
    elif score_player > score_computer and score_player <= ventuno and score_computer >= 19:
        random_roller = random.randrange(1,3)
        return random_roller
    elif player_stays and score_player < score_computer or score_computer >= 18:
        return stay
    elif score_player == score_computer and 18 <= score_player <= ventuno and 18 <= score_computer <= ventuno:
        random_roll = random.randrange(1,3)
        return random_roll
    elif score_computer < 18:
        return roll

#--------------------------------------------------------------
#--------------------------------------------------------------
# DO NOT CHANGE THE CODE BELOW THIS LINE
#--------------------------------------------------------------
#--------------------------------------------------------------
def play_a_game(player_name):
    ventuno = 21

    player_stays = False
    computer_stays = False

    roll = 1
    stay = 2

    score_player = get_starting_score()
    score_computer = get_starting_score()

    current_player = get_random_starting_player_name(player_name)
    display_current_scores(" " * 5, score_player, score_computer, player_stays, computer_stays, player_name)

    while not game_is_over(score_player, score_computer, player_stays, computer_stays):
        if current_player == "Computer":
            if not computer_stays:
                display_current_player(" " + current_player)
                selection = get_computer_selection(score_player, score_computer, player_stays)

                if selection == roll:
                    score_computer = add_dice_roll(score_computer, "  Computer")
                    if score_computer == ventuno:
                        computer_stays = True
                else:
                    computer_stays = True
        elif not player_stays:
            display_current_player(" " + current_player)
            selection = get_play_menu_selection(' ' * 3)
            print()
            if selection == roll:
                score_player = add_dice_roll(score_player, " " + player_name)
                if score_player == ventuno or (computer_stays and score_player > score_computer):
                    player_stays = True
            elif selection == stay:
                player_stays = True

        display_current_scores(" " * 5, score_player, score_computer, player_stays, computer_stays, player_name)
        current_player = get_next_player(current_player, player_name)


    game_winner = get_winner_name(score_player, score_computer, player_name)
    display_game_result("  ", score_player, score_computer, game_winner, player_name)
    return game_winner

main()
