import random

"""
This program simulates the "Rock, Paper, Scissors" game. 
"""

def play():
    # The user is prompted for a choice, and the computer randomly chooses.
    user = input("Pick one... \n'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    # This shows the user's choice and the computer's choice
    print("You: "+user)
    print("Computer: "+computer)

    if user == computer:
        return '\nIt\'s a tie'
    
    if is_win(user, computer):
        return '\nYou won!'
    
    return '\nYou lost!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


# This variable keeps the game loop going
keep_playing = "y" 

# This is the game loop
while(keep_playing != "n"):
    print(play())
    keep_playing = input("\nWould you like to keep playing? 'y' for yes, 'n' for no\n").lower()


print("Goodbye!")
