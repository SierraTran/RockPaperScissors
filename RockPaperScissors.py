import random

"""
This program simulates the "Rock, Paper, Scissors" game. 
"""

def play():
    # The user is prompted for a choice, and the computer randomly chooses.
    user = input("Pick one... \nType 'r' for rock, 'p' for paper, or 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    # This variable uses the is_valid_choice function to make sure the user input can be used for the game
    valid_choice_play = is_valid_choice_play(user)
    
    # If the user inut is not valid, this loop will start and run until valid input is received from the user
    while(valid_choice_play == False):
        print(user + " is not a valid choice. Please try again.")
        user = input("Pick one... \nType 'r' for rock, 'p' for paper, or 's' for scissors\n").lower()
        valid_choice_play = is_valid_choice_play(user)

    # This shows the user's choice and the computer's choice
    print("You: " + user)
    print("Computer: " + computer)

    if user == computer:
        return '\nIt\'s a tie'
    
    if is_win(user, computer):
        return '\nYou won!'
    
    return '\nYou lost!'
    
"""
This function determines if the player has won based on the three possible win cases.
It returns true if one of these cases have been achieved.
"""
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

"""
This function returns true if the user inputs 'r', 'p', or 's', 
and returns false if it is anything else
"""
def is_valid_choice_play(player):
    if (player == 'r') or (player == 'p') or (player == 's'):
        return True
    return False

def player_continue():
    answer = input("\nWould you like to keep playing? Type 'y' for yes or 'n' for no.\n").lower()

    valid_choice_continue = is_valid_choice_player_continue(answer)

    while(valid_choice_continue == False):
        print(answer + " is not a valid choice. Please try again.")
        answer = input("Would you like to keep playing? Type 'y' for yes or 'n' for no.\n").lower()
        valid_choice_continue = is_valid_choice_player_continue(answer)

    if answer == 'y':
        return True
    return False

def is_valid_choice_player_continue(answer):
    if (answer == 'y') or (answer == 'n'):
        return True
    return False

# This variable keeps the game loop going
keep_playing = True

# This is the game loop
while(keep_playing):
    print(play())
    keep_playing = player_continue()

print("Goodbye!")
