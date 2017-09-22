import math
import random

# config
low = 1
high = 100
limit = math.ceil(math.log(high-low+1, 2))  

# helper functions
def show_start_screen():
    print("   _____                               _   _                 _               _ ") 
    print("  / ____|                             | \ | |               | |             | |") 
    print(" | |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __| |") 
    print(" | | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |")  
    print(" | |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |  |_|")  
    print("  \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)")  
                                                                                   

def show_credits():
    print("This awesome game was created by ")
    print("  _______    _                   _____ ")                                
    print(" |__   __|  | |                 |  __ \ ")                               
    print("    | | __ _| |_ ___ _ __ ___   | |__) |__  __ _ _ __ ___  ___  _ __ ") 
    print("    | |/ _` | __/ _ \ '_ ` _ \  |  ___/ _ \/ _` | '__/ __|/ _ \| '_ \\")   
    print("    | | (_| | ||  __/ | | | | | | |  |  __/ (_| | |  \__ \ (_) | | | |")
    print("    |_|\__,_|\__\___|_| |_| |_| |_|   \___|\__,_|_|  |___/\___/|_| |_|") 
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print("You will have " + str(limit) + " attempts to guess the number.") 

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
        print("    ./**, ,******,.  .,*/(*,((,.   ")   
        print("   ,    * .**,*,,,.  .,*/(/,   ,   ")   
        print("    *    ..,,,,,,,.  .,*/(     ,   ")   
        print("    .*     .,,,,,,.  .,/(#    ,    ")   
        print("      ,.  , ..,,,,. .,*(#,  ..     ")   
        print("        ,. ...,,*,...,/(( ..       ")   
        print("           ...,,**,,,*//,          ")   
        print("             * ,,****/*            ")   
        print("           ,.. .,**/  *            ")   
        print("                 ,*                ")   
        print("                ,,,                ")   
        print("                ,.*                ")   
        print("                * *                ")   
        print("              ,**.,/*              ")   
        print("           *@@@@@@@@@@@&           ")   
        print("           /&,,,..... %&           ")   
        print("           /%,,,,,,,..%&           ")   
        print("           &&&&&&&&&&&&&           ") 
    else:
        print("Too bad! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ") 
        decision= decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
