import random
import datetime
from time import time,sleep

def print_pause(text):
    print(text)
    sleep(2)

def print_quick(text):
    print(text)
    sleep(1)

def print_quicker(text):
    print(text)
    sleep(0.5)

def print_quickest(text):
    print(text)
    sleep(0.1)


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

def monsters(monster_types, villian):
    """
    Returns a random monster for the duration of the story
    """
    if villian == monster_types[0] :
        pass # Function for monsters
    elif villian == monster_types[1] :
        pass # Function for monsters
    elif villian == monster_types[2] :
        pass # Function for monsters
    elif villian == monster_types[3] :
        pass # Function for monsters
    elif villian == monster_types[4] :
        pass # Function for monsters
    elif villian == monster_types[5] :
        pass # Function for monsters
    elif villian == monster_types[6] :
        pass # Function for monsters
    elif villian == monster_types[7] :
        pass # Function for monsters


def ending(best_friend, afraid,):
    print_pause("Quickly you run to the portal before it closes")
    print_pause("You made it!!")
    print_pause(f"Just as you pass through you see {best_friend} been pulled into the Phantasm Void by {afraid}.")
    play_again = choice("Do you want to play again? (yes OR no)","yes","no")
    return play_again


def the_story(name, best_friend, gender, afraid):
    today = datetime.datetime.now()
    t_day = today.day
    t_month = today.month
    t_year = today.year
    t_hour = today.hour
    t_mins = today.minute
    awake = "no"
    snooze = 0

    villian = (name[len(name)::-1]).lower() # Slicing the name to create a mirror copy
    if gender == "male":
        villian_gender = "female"
    else:
        villian_gender = "male"

    if afraid == '': # This way if there is no input it regsiters as 'nothing', which would also make an intersting story
        afraid = "Nothing"
    chosen = random.randint(0,7)
    monster_types = ["Goblin King", "Broken Clown", "Hydra Spider", "ArGru", "Upside-down Teletubby", "Malfunctioning Robot", "Death", "Shark with Gummy Bear teeth"]
    monster_types.append(afraid)
    villian_type = monster_types[chosen]
    monsters(monster_types,villian)

    # And so it begins
    print_quick("Quickly you run to the portal before it closes")
    print_quick("You made it!!")
    print_quick(f"Just as you pass through you see {best_friend} been pulled into the Phantasm Void by {afraid}.")
    print_quicker(f"You scream {best_friend.upper}!!")

    print_quickest("BRRRRR....")
    print_quickest("BRRRRRRR....BRRRRRRRR")
    print_pause("*YAWN*")
    print_pause("You wake up, unsure what day it is")
    print_pause(f"You check you phone and see it's {t_day}/{t_month}/{t_year}")
    
    while awake == "no": # Notice how I don't mention the date again ;)
        print_pause(f"The time is {t_hour}:{t_mins}")
        awake = choice("Do you want to get out of bed? (yes OR no)","yes","no")
        rand_mins = random.randint(1,20)
        rand_hour = random.randint(0,1)
        if ((t_mins + rand_mins) % 60) != (t_mins + rand_mins): # This way if the mins go past 60 it add an extra hour
            t_mins = (t_mins + rand_mins) %60
            t_hour += 1
        t_hour = (t_hour + rand_hour) %24
        snooze += 1
    
    print_pause("You're finally up!")
    print_pause("After going to the bathrom and having your shower, you realise today is going to be a hot day")
    clothes = choice("Would you like to wear some clothes? (yes OR no)","yes","no")
    
    if clothes == "no": # This is where the gender comes into play
        print_pause("You've decided to go wild and strut in the nude")
    else:
        if gender == "male":
            print_pause("You pick you favourite top and jogging bottoms to wear")
        else:
            print_pause("You picked your favourite top and shorts to wear")
    
    print_pause("Just us you sit down to check your what's happening on social media")
    print_pause("You hear a loud crash and the room starts shaking")
    print_pause("Afraid that your house would crumble on top of you")
    print_pause("You step outside to see just what's happening")
    print_pause("To your suprise you realise you're not at home")
    print_pause("Everything is the wrong way around")
    print_pause("Cats are as tall as trees")
    print_pause("Birds are tunelling from the ground up")
    print_pause("Trees are falling from the sky, with the weight of a pillow...only to disappear once they touch the ground")
    print_pause("You've resolved yourself to finding your way home and walk out of the cul-de-sac")
    print_pause("You are met with a fork in the road")
    fork = choice("Do you want to go left or right?", "left", "right")
          
    


def lets_play():
    '''
    Main funcion 
    '''

    # Calling all variables required
    print_pause("Welcome to your Story")
    print_pause("A few house rules:")
    print_pause("   1) When a prompt is required the console will display '...' in front of an empty line")
    print_pause("   2) Answers are accepted in a single work e.g. yes, no, open etc.")
    print_pause("   3) Once you've entered an answer, press the 'ENTER' or 'RETURN' key\n")
    print_pause("Before we begin, could you tell us:")
    name = input(" - What's your name:\n...")
    best_friend = input(" - What's your best friend's name:\n...")
    gender = choice(" - Are you male or female?","male","female")
    afraid = input(" - What are you afraid of?\n...")
    
    # The game starts from here
    play = choice("Are you ready to begin?(yes OR no)","yes","no")
    played = 0
    start_time = time()

    while play == "yes":
        the_story(name,best_friend, gender, afraid)
        played +=1
        play = ending(best_friend, afraid)

    end_time = time()
    total_time = end_time - start_time # Calculates the total amount of time taken
    t_hours = int(total_time / 3600) # 3600 seconds in 1 t_hour
    t_hourless = total_time % 3600 # remainder to calculate minutes and seconds
    minutes = int(t_hourless / 60 ) # 60 seconds in a minute
    seconds = round(t_hourless % 60) # what's left will equal seconds

    print (f"Well done, you completed {played} game run(s) in {t_hours}h:{minutes}m:{seconds}s")
    


lets_play()





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