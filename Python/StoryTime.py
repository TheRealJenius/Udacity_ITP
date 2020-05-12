import random
import datetime
from time import time,sleep

def print_pause(text):
    print(text)
    sleep(2)

def print_quick(text):
    print(text)
    sleep(0.5)

def choice(text,a = "yes",b = "no"):
    """
    Gives the user a choice
    If the choice isn't taken, one is randomly picked after 4 attempts
    """
    valid = False
    retry = 0
    while valid == False:
        chosen = input(text + "\n...").lower()
        if chosen == a.lower():
            valid = True
            return chosen
        elif chosen == b.lower():
            valid = True
            return chosen
        else:
            retry +=1
        
        if retry >= 4:
            forced = random.randint(1,2)
            if forced == 1:
                forced_choice = a
            elif forced == 2:
                forced_choice = b
            print_pause(f"Due to {retry} invalid choices, the system has chosen '{forced_choice}' for you...good luck.")
            valid = True
            return forced_choice

def Monsters(FearToAdd):
    """
    Returns a random monster for the duration of the story
    """
    if FearToAdd = '':
        FearToAdd = "Nothing"
    chosen = random.randint(0,7)
    MonsterTypes = ["Goblin King", "Broken Clown", "Hydra Spider", "ArGru", "Upside-down Teletubby", "Malfunctioning Robot", "Death", "Shark with Gummy Bear teeth"]
    MonsterTypes.append(FearToAdd)
    print(MonsterTypes)


def intro():
    Today = datetime.datetime.now()
    Day = Today.day
    Month = Today.month
    Year = Today.year
    Hour = Today.hour
    Mins = Today.minute
    print_pause("*YAWN*")
    print_pause(f"You wake up on {Day}/{Month}/{Year}")
    print_pause(f"The time is {Hour}:{Mins}")
    choice("Do you want to wakeup (yes OR no)?","yes","no")
    


def LetsPlay():
    ''' 
    Main funcion 
    '''

    # Calling all variables required
    start_time = time()
    print_pause("Before we begin, could you tell us:\n...")
    Name = input("What's your name:\n...")
    Gender = choice("Are you male or female?","male","female")
    Fear = input("What are you afraid of?\n")
    Villian = (Name[len(Name)::-1]).lower() # Slicing the name to create a mirror copy
    if Gender == "male":
        Villian_Gender = "female"
    else:
        Villian_Gender = "male"
    
    Monsters(Fear)

    # The game starts from here
    intro()
    
    end_time = time()
    total_time = end_time - start_time # Calculates the total amount of time taken
    hours = int(total_time / 3600) # 3600 seconds in 1 hour
    hourless = total_time % 3600 # remainder to calculate minutes and seconds
    minutes = int(hourless / 60 ) # 60 seconds in a minute
    seconds = round(hourless % 60) # what's left will equal seconds

    print (f"Well done, you completed the game in {hours}h:{minutes}m:{seconds}s")
    


LetsPlay()





'''
Output text to the console.
    Descriptions are printed to the console for the player to see.

Import modules and use functions from those modules.
	The time.sleep function is used to create delays between messages so that they aren't all printed at once.
    The random.choice or random.randint function is used to influence the game so that each game is different in some way.

Use the input function in combination with conditional statements (e.g., if and while) to create an interactive program.
    The input function is used to ask the player what they would like to do.
    The player's choices affect what happens in the game, including:
        Whether the player wins or loses
        Whether to restart or exit after the game is over

Use a conditional loop to handle invalid input.
	If the player enters a choice that is not valid, the game gives them the chance to retry until they enter a valid option.
    The game does not crash and does not treat invalid input as a valid choice.

Refactor code by defining and calling functions.
	The code includes at least four function definitions that are used to improve the code in some way, such as by:
        Reducing repetition
        Reducing complexity
        Improving the readability or organization of the code
    Each function should have a single purpose and a name that describes that purpose.

Write code that follows the standard Python style guide.
    The pycodestyle tool reports zero errors and zero warnings.

Test code and produce an error-free program.
	The program is a playable game, and runs from start to finish without crashing or displaying errors.
 '''