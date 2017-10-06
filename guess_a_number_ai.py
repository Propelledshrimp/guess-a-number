import random
#Guess a Number AI
#Tatem P 

# config
low = 1
high = 100
# helper functions

def show_start_screen():
    print(" _____                               _   _                 _                  ___  _____   _ ") 
    print("|  __ \                             | \ | |               | |                / _ \|_   _| | |") 
    print("| |  \/_   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __  / /_\ \ | |   | |") 
    print("| | __| | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |  _  | | |   | |")        
    print("| |_\ \ |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |    | | | |_| |_  |_|") 
    print(" \____/\__,_|\___||___/___/  \__,_| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|    \_| |_/\___/  (_)")

def set_difficulty():
    difficulty = input("Before we get started, please choose a difficulty. Easy, Medium, or Hard: ")
    difficulty = difficulty.lower()
    difficulty = difficulty.strip()
    return difficulty 

def show_credits():
    print("This AI that may or may not take over the world was created by")
    print("  _______    _                   _____ ")                                
    print(" |__   __|  | |                 |  __ \ ")                               
    print("    | | __ _| |_ ___ _ __ ___   | |__) |__  __ _ _ __ ___  ___  _ __ ") 
    print("    | |/ _` | __/ _ \ '_ ` _ \  |  ___/ _ \/ _` | '__/ __|/ _ \| '_ \\")   
    print("    | | (_| | ||  __/ | | | | | | |  |  __/ (_| | |  \__ \ (_) | | | |")
    print("    |_|\__,_|\__\___|_| |_| |_| |_|   \___|\__,_|_|  |___/\___/|_| |_|")
    print(" __  _____             ____            _____  _____  __   ______")
    print("/  ||  _  |           / ___|          / __  \|  _  |/  | |___  /") 
    print("`| || |/' |  ______  / /___   ______  `' / /'| |/' |`| |    / / ") 
    print(" | ||  /| | |______| | ___ \ |______|   / /  |  /| | | |   / /  ") 
    print("_| |\ |_/ /          | \_/ |          ./ /___\ |_/ /_| |_./ /   ")
    print("\___/\___/           \_____/          \_____/ \___/ \___/\_/    ") 
                                                             

    
def get_guess(current_low, current_high, difficulty):
    """
    Return a truncated average of current low and high.
    """
    if difficulty == "easy":
        guess = random.randint(current_low, current_high)
        return guess

    elif difficulty == "medium":
         for guess in range(current_low, current_high):
                 guess = (current_low + current_high)//2
                 if(guess%5 >=0) and (current_high - current_low > 5):
                    guess = (guess//5)*5
                    return guess
                 elif (current_high - current_low <= 5): 
                     guess = random.randint(current_low, current_high)
                     return guess
          
    
    elif difficulty == "hard":
       guess = (current_low + current_high)//2
       return guess 


def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    number = input("Think of a number between " + str(low) + " and " + str(high) + " and I will try to guess it. Press Enter when you have your number." )
    

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.
    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
  
    while True :
        print(str(guess))
        check_number = input("Is this number too high, too low, or correct? Answer high, low, or correct: ")
        check_number = check_number.lower()
        check_number = check_number.strip() 
        
        if check_number == "low" or check_number == "low ": 
            return -1
        elif check_number == "correct" or check_number == "correct " :
            return 0
        elif check_number == "high" or check_number == "high ": 
            return 1
        else:
            print("Please use a valid input.") 
        

     

def show_result(check, tries):
    if check == 0:
        print("It took me " + str(tries) + " attempt(s) to guess your number.")  

def play_again():
    while True: 
        decision = input("I won, inferior human. Would you like to play again? (y/n) ")
        decision = decision.lower()
        decision = decision.strip() 
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
    tries = 1 
    difficulty = set_difficulty()
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high, difficulty)
        check = check_guess(guess)

        if check == -1:
            current_low = guess + 1
            tries+= 1
           
        elif check == 1:
            current_high = guess - 1
            tries += 1
         
    show_result(check, tries) 

    


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

