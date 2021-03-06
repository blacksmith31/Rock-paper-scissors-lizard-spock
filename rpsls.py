# Rock-paper-scissors-lizard-Spock 


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random as rand
# helper functions

def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print "Error - enter a correct name inside quotation marks."
    
    return number


    # convert name to number using if/elif/else

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print "Error number not in the range 0 to 4 inclusive"

    return name

    # convert number to a name using if/elif/else

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print
    
    # print out the message for the player's choice
    print 'Player choice: ' + str(player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
   
    # compute random guess for comp_number using random.randrange()
    comp_number = rand.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer choice: ' + str(comp_choice)
    
    # compute difference of comp_number and player_number modulo five
    diff = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print "Player wins!!"
    elif diff == 3 or diff == 4:
        print "Computer wins"
    else:
        print "Tie"
        
player = input("Enter 'rock', 'paper', 
'scissors', 'lizard', or 'spock': ")

rpsls(player)


