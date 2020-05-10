# GUI-based version of RPSLS

###################################################

import simplegui
import random


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
    return number    

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
    return name  

def rpsls(player_choice): 

    # print a blank line to separate consecutive games
    print "\n"
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print 'Computer chooses ' + computer_choice
    # compute difference of comp_number and player_number modulo five
    compare = (player_number - comp_number) % 5
    # use if/elif/else to determine winner, print winner message
    print compare
    
    if (compare == 1) or (compare == 2):
        print 'Player wins!'
    elif (compare == 3) or (compare == 4):
        print 'Computer wins!'
    elif( compare == 0):
        print 'tie'

# handler for button field
def rock():
    rpsls("rock")
def spock():
    rpsls("Spock")
def paper():
    rpsls("paper")
def lizard():
    rpsls("lizard")
def scissors():
    rpsls("scissors")
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)

frame.add_button("rock", rock, 100)
frame.add_button("Spock", spock, 100)
frame.add_button("paper", paper, 100)
frame.add_button("lizard", lizard, 100)
frame.add_button("scissors", scissors, 100)


# Start the frame animation
frame.start()



###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
