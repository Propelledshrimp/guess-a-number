import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_low + current_high)//2
    return guess 
    

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    number = input("Think of a number between " + str(low) + " and " + str(high) + " and I will try to guess it: " )
     

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.
    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print(str(guess))
    check_number = input("Is this number too high, too low, or correct? Answer high, low, or correct: ")
    check_number = check_number.lower() 
    if check_number == "low":
        check = -1
    elif check_number == "correct":
        check = 0
    elif check_number == "high":
        check = 1

    return check 

def show_result(check_number):
    if check_number == "correct" :
        print("I won, inferior human.") 

def play_again():
    while True:
        decision = input("I won, inferior human. Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = guess + 1
            pass
        elif check == 1:
            current_high = guess - 1
            


    


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

