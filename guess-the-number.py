# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

answer = 100
counter = 7

def new_game():
    global answer, counter
    answer = random.randrange(100)
    counter = 7
    f.start()
    print ""
    print "new game answer is", answer

    
def input_guess(guess):
    # main game logic goes here	
    global counter
    print "Guess was " + guess
    guess = int(guess)
     
    if guess < answer:
        print "higher"
        counter = counter - 1
        print "You have", counter, "Life left"
    elif guess > answer:
        print "lower"
        counter = counter - 1
        print "You have", counter, "Life left"
    else:
        print "You won"
        new_game()
    
    if counter <=0:
        print "No more life, You Lost"
        new_game()
    return
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("New Game", new_game, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
