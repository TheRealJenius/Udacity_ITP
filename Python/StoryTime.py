import random
import datetime
from time import time, sleep


# I've placed the time on top as it allows me have more control
# on the actual text being printed, instead of the text following it
def print_pause(text):
    '''
    Print within 1.5 seconds of being called
    '''
    sleep(1.5)
    print(text)


def print_quick(text):
    '''
    Print within 1 second of being called
    '''
    sleep(1)
    print(text)


def print_quicker(text):
    '''
    Print within 0.5 seconds of being called
    '''
    sleep(0.5)
    print(text)


def print_quickest(text):
    '''
    Print within 0.1 seconds of being called
    '''
    sleep(0.1)
    print(text)


def choice(text, a, b):
    """
    Gives the user a choice
    If the choice isn't taken, one is randomly picked after 4 attempts
    """
    valid = False
    retry = 0
    while valid is False:
        chosen = input(text + "\n...").lower()
        if chosen == a.lower():
            valid = True
            return chosen
        elif chosen == b.lower():
            valid = True
            return chosen
        else:
            retry += 1

        if retry >= 4:
            forced = random.choice([a, b])
            print_pause(f"Due to {retry} invalid choices, "
                        "the system has chosen "
                        f"'{forced}' for you...good luck.")
            valid = True
            return forced


def quiz(text, answer, prize):
    """
    Gives the user 1 more chance to answer the quiz question correctly
    """
    valid = False
    retry = 0
    while valid is False:
        chosen = input(text + "\n...").lower()
        if chosen == answer.lower():
            print_quick("\nWell done!!")
            print_pause(f"You've received the {prize}")
            valid = True
            return prize  # They get the prize added to their arsenal
        else:
            retry += 1
            print_quick("\nYour answer was incorrect, try once more")

        if retry > 1:
            print_pause("\nSadly you failed to answer the question correctly")
            print_pause(f"The correct answer is {answer}")
            valid = True
            return ""  # This means they didn't answer the quiz correctly


def monsters(image_required):
    """
    Displays the image of the villain
    """
    if image_required == "the Goblin King":
        print("             ,      ,")
        print("            /(.-\"\"-.)\\")
        print("        |\\  \\/      \\/  /|")
        print("        | \\ / =.  .= \\ / |")
        print("        \\( \\   o\\/o   / )/")
        print("         \\_, '-/  \\-' ,_/")
        print("           /   \\__/   \\")
        print("           \\ \\__/\\__/ /")
        print("         ___\\ \\|--|/ /___")
        print("       /`    \\      /    `\\")
        print("      /       '----'       \\")
    elif image_required == "the Broken Clown":
        print("              ,-.  _")
        print("    _________/_  \\( )_")
        print("    \\       / / (_ O _)")
        print("     )=====@=(    (_)")
        print("____/_________\\____")
        print("    | /~\\ /~\\ |")
        print("   _| \\a/_\\a/ |_")
        print("  (_  _'(_) _  _)")
        print("    \\( \\___/ )/")
        print("     \\\\ ,-. //")
        print("   __ \\\\___// __")
        print("  |* *--._,--'* |")
        print("  | * * (_)* * *|")
        print("  |* ,-'   `-.* |")
        print("  `./         \\,'")
    elif image_required == "the Hydra Spider":
        print("                   /\\              _")
        print("                  /  \\            / \\")
        print("                 |  _ \\          /   \\   _")
        print("                 | / \\ \\        /     \\ / \\")
        print("                 |/   \\ \\       |      /   \\")
        print("                 /     \\ |      | /\\  / \\   \\")
        print("                /|      \\| ~  ~ |/  \\/   \\   \\")
        print("        _______/_|_______\\(o)(o)/___/\\___|_   \\")
        print("       /      /  |       (__-___)     \\  | \\   \\_")
        print("      /      /   |      /              \\ |  \\")
        print("     /      /    |     /                \\|   \\")
        print("    /      /     |    /                  \\    \\")
        print("   /     _/      |   /                   |\\    \\")
        print("  /             _|  |                    |_\\    \\_")
        print("_/                  |                       \\")
        print("                    |                        \\")
        print("                    |                         \\_")
        print("                   _|                        ")
    elif image_required == "the ArGru Conqueror":
        print("                            ==(W{==========-      /===-")
        print("                              ||  (.--.)         /=="
              "=-_---~~~~~~~~~------____")
        print("                              | \\_,|**|,__      |=="
              "=-~___                _,-'`")
        print("                 -==\\\\        `\\ ' `--'   ),    `"
              "//~\\\\   ~~~~`---.___.-~~")
        print("             ______-==|        /`\\_. .__/\\ \\    |"
              " |  \\\\           _-~`")
        print("       __--~~~  ,-/-==\\\\      (   | .  |~~~~|   | "
              "|   `\\        ,'")
        print("    _-~       /'    |  \\\\     )__/==0==-\\<>/   / "
              "/      \\      /")
        print("  .'        /       |   \\\\      /~\\___/~~\\/  /' "
              "/        \\   /'")
        print(" /  ____  /         |    \\`\\.__/-~~   \\  |_/'  / "
              "         \\/'")
        print("/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`")
        print("                  \\_|      /        _) | ;  ),   __--~~")
        print("                    '~~--_/      _-~/- |/ \\   '-~ \\")
        print("                   {\\__--_/}    / \\\\_>-|)<__\\      \\")
        print("                   /'   (_/  _-~  | |__>--<__|      |")
        print("                  |   _/) )-~     | |__>--<__|      |")
        print("                  / /~ ,_/       / /__>---<__/      |")
        print("                 o-o _//        /-~_>---<__-~      /")
        print("                 (^(~          /~_>---<__-      _-~")
        print("                ,/|           /__>--<__/     _-~")
        print("             ,//('(          |__>--<__|     /       "
              "           .----_")
        print("            ( ( '))          |__>--<__|    |        "
              "         /' _---_~\\")
        print("         `-)) )) (           |__>--<__|    |        "
              "       /'  /     ~\\`\\")
        print("        ,/,'//( (             \\__>--<__\\    \\    "
              "        /'  //        ||")
        print("      ,( ( ((, ))              ~-__>--<_~-_  ~--____"
              "---~' _/'/        /'")
        print("    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/")
        print("  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~")
        print("   ;'( ')/ ,)(                              ~~~~~~~~~~")
        print("  ' ') '( (/")
        print("    '   '  `        ")
    elif image_required == "the Upside-down Teletubby":
        print("         ,-˙‾‾‾‾‾‾‾‾‾˙-,         ")
        print("        ˙,             ,˙        ")
        print("          > ,-,˙‾˙,-, <          ")
        print("     ,--,˙,˙ /--^--\\ ˙,˙,--,     ")
        print("    //‾/ /      ⅄      \\ \\‾\\\\    ")
        print("   //  ||  ,--,   ,--,  ||  \\\\   ")
        print("   || ,||  \\()|   |()/  ||, ||   ")
        print("   ||/,\\ \\  ‾‾     ‾‾  / /,\\||   ")
        print("   ˙-˙  \\ ˙,         ,˙ /  ˙-˙   ")
        print("        ˙, ˙-,,, ,,,-˙ ,˙         ")
        print("          ˙˙--,, ,,--˙˙           ")
        print("               | |               ")
        print("               | |               ")
        print("               | |               ")
        print("               ˙-˙               ")
    elif image_required == "the Circle of oOoOo":
        print("                  ooo OOO OOO ooo")
        print("               oOO                 OOo")
        print("           oOO                         OOo")
        print("        oOO                               OOo")
        print("      oOO                                   OOo")
        print("    oOO                                       OOo")
        print("   oOO                                         OOo")
        print("  oOO                                           OOo")
        print(" oOO                                             OOo")
        print(" oOO                                             OOo")
        print(" oOO                                             OOo")
        print(" oOO                                             OOo")
        print(" oOO                                             OOo")
        print("  oOO                                           OOo")
        print("   oOO                                         OOo")
        print("    oOO                                       OOo")
        print("      oOO                                   OOo")
        print("        oO                                OOo")
        print("           oOO                         OOo")
        print("               oOO                 OOo")
        print("                   ooo OOO OOO ooo")
    elif image_required == "Death's Cousin":
        print("               ...")
        print("             ;::::;")
        print("           ;::::; :;")
        print("         ;:::::'   :;")
        print("        ;:::::;     ;.")
        print("       ,:::::'       ;           OOO\\")
        print("       ::::::;       ;          OOOOO\\")
        print("       ;:::::;       ;         OOOOOOOO")
        print("      ,;::::::;     ;'         / OOOOOOO")
        print("    ;:::::::::`. ,,,;.        /  / DOOOOOO")
        print("  .';:::::::::::::::::;,     /  /     DOOOO")
        print(" ,::::::;::::::;;;;::::;,   /  /        DOOO")
        print(";`::::::`'::::::;;;::::: ,#/  /          DOOO")
        print(":`:::::::`;::::::;;::: ;::#  /            DOOO")
        print("::`:::::::`;:::::::: ;::::# /              DOO")
        print("`:`:::::::`;:::::: ;::::::#/               DOO")
        print(" :::`:::::::`;; ;:::::::::##                OO")
        print(" ::::`:::::::`;::::::::;:::#                OO")
        print(" `:::::`::::::::::::;'`:;::#                O")
        print("  `:::::`::::::::;' /  / `:#")
        print("   ::::::`:::::;'  /  /   `#")
    elif image_required == "the Shark with Gummy Bear teeth":
        print("                             ,_.")
        print("                           ./  |                      "
              "                    _-")
        print("                         ./    |                      "
              "                 _-'/")
        print("      ______.,         ./      /                      "
              "               .'  (")
        print(" _---'___._.  '----___/       (                       "
              "             ./  /`'")
        print("(,----,_  G \\                  \\_.                  "
              "             ./   :")
        print(" \\___   \"--_                      \"--._,           "
              "            ./    /")
        print(" /^^^^^-__          ,,,,,               \"-._       /|"
              "         /     /")
        print(" `,       -        /////                    \"`--__/ ("
              "_,    ,_/    ./")
        print("   \"-_,           ''''' __,                          "
              "  `--'      /")
        print("       \"-_,             \\\\ `-_                     "
              "             (")
        print("           \"-_.          \\\\   \\.                  "
              "               \\_")
        print("          /    \"--__,      \\\\   \\.                "
              "       ____.     \"-._,")
        print("         /        ./ `---____\\\\   \\.______________,"
              "---\\ (     \\,        \"-.,")
        print("        |       ./             \\\\   \\        /\\  |"
              "     \\|       `--______---`")
        print("        |     ./                 \\\\  \\      /_/\\_!")
        print("        |   ./                     \\\\ \\")
        print("        |  /                         \\_\\")
        print("        |_/")
    elif image_required == "the Nothingness Paradox":
        print("       ___                  ____                  ___")
        print("  ____(   \\              .-'    `-.              /   )____")
        print(" (____     \\_____       /  (O  O)  \\       _____/     ____)")
        print("(____            `-----(      )     )-----'            ____)")
        print(" (____     _____________\\  .____.  /_____________     ____)")
        print("   (______/              `-.____.-'              \\______)")
    else:  # this is when it matches with the user's fear
        print("                                _,.-----.,_")
        print("                             ,-~           ~-.")
        print("                           ,^___           ___^.")
        print("                          /~\"   ~\"   .   \"~   \"~\\")
        print("                         Y  ,--._    I    _.--.  Y")
        print("                         | Y     ~-. | ,-~     Y |")
        print("                         | |        }:{        | |")
        print("                         j l       / | \\       ! l")
        print("                      .-~  (__,.--\" .^. \"--.,__)  ~-.")
        print("                     (           / / | \\ \\           )")
        print("                      \\.____,   ~  \\/\"\\/  ~   .____,/")
        print("                       ^.____                 ____.^")
        print("                          | |T ~\\  !   !  /~ T| |")
        print("                          | |l   _ _ _ _ _   !| |")
        print("                          | l \\/V V V V V V\\/ j |")
        print("                          l  \\ \\|_|_|_|_|_|/ /  !")
        print("                           \\  \\[T T T T T TI/  /")
        print("                            \\  `^-^-^-^-^-^'  /")
        print("                             \\               /           ")
        print("                              \\.           ,/")
        print("                                \"^-.___,-^\"")
        print("")


def ending(player, villain):
    if player[13] > 0:  # secret ending - because every good story needs one ;)
        print_quick("\nYou look around and see that you are in a laboratory, "
                    "in what used to be your attic")
        print_quick("You look around the laboratory and find a pod with "
                    "something inside")
        print_quick(f"It's {player[8]}!!")
        print_quick("GASP!\n")
        print_quick("You search around and find a release switch")
        print_quicker(f"{player[8]} wakes up, they hug you with joy after "
                      "being freed from the pod")
        print_quicker("You grab them and you both hurriedly "
                      "search for the exit")
        print_quicker("You see a light shining from behind the pod\n")
        print_quicker(f"With the help of {player[8]} you manage to move "
                      "the pod and find an exit")
        print_quicker("It's a wormhole!?")
        print_quicker("Looking at each other, you decide to jump through")
        print_quickest("~\n" * 3)
        print_quicker("You made it back!!")
        print_quicker("You're back on Earth!!")
        print_quicker("Congratulations you won and discovered "
                      "the secret ending!!!\n")
        player[12] = choice("Do you want to play again? "
                            "(yes OR no)", "yes", "no")
        return player
    elif villain[3] == "":  # lose condition
        print_quicker("\nUnfortuantely you failed to win the battle aginst "
                      f"{villain[0]} {villain[2]}")
        print_quicker("Staring down at you, they bite your head off")
        player[12] = choice("\nDo you want to play again? "
                            "(yes OR no)", "yes", "no")
        return player
    elif villain[3] == "defeated":  # win condition 1
        print_quicker("\nYou run into your house to make sure "
                      f"{villain[0]} {villain[2]} is really dead")
        print_quicker("You poke at the corpse and feel satisfied that "
                      "they are finally dead")
        print_quicker("You start searching around for a means of escpae "
                      "from this world")
    elif villain[3] == "escaped":  # win condition 2
        print_quicker("\nYou search around the house for a clue to escape")
        print_quicker("You hear the thumping getting louder, "
                      f"{villain[0]} {villain[2]} might just breakthrough")

    print_quicker("\nFrom the corner of your eye, you see something glowing")
    print_quicker("It's a portal and it's closing")
    print_pause("\nQuickly you run to the portal before it closes")
    print_pause("You made it!!")
    print_pause(f"\nJust as you pass through you see {player[8]} been pulled "
                f"into the Phantasm Void by {player[2]}.\n")
    player[12] = choice("Do you want to play again? "
                        "(yes OR no)", "yes", "no")
    return player


def middle(player):
    '''
    The middle section of the game, where the player can gear up
    '''
    # resetting these 3 list variables incase they choose to play again
    player[5] = ""
    player[6] = ""
    player[7] = ""

    if player[10] == "left":
        print_pause(f"\nAs you head {player[10]} on the road you come across a"
                    " strange lady who looks to be talking to herself")
        print_quick("You approach them")
        print_quick("Suddenly they turn")
        print_pause("Appraising you from head to toe, they smile a "
                    "coy smile at you")
        quizzes = choice("Would you like to ask them for help? "
                         "(yes OR no)", "yes", "no")
        if quizzes == "yes":
            print_pause("They strange lady asks you the following "
                        "three questions:")
            player[6] = quiz("\n1) What is in the middle of March and April, "
                             "that can't be seen at the beginning or end of "
                             "either month?", "r", "Sonic Shoes")
            player[7] = quiz("\n2) Can you find the\nthe mistake:"
                             "\n1,2,3,4,5,6", "the", "Time Stopping Watch")
            player[5] = quiz("\n3) I have cities, but no houses. I "
                             "have mountains, but no trees. I have water, "
                             "but no fish. "
                             "I am a _______?", 'map', "Enigma Cracker")
        else:
            print_pause("\nYou decide to continue on your journey to escape")

    else:
        print_pause(f"\nAs you head {player[10]} on the road you come across a"
                    " strange man who looks to be talking to himself")
        print_quick("You approach them")
        print_quick("Suddenly they turn")
        print_pause("Appraising you from head to toe, they smile a "
                    "coy smile at you")
        quizzes = choice("Would you like to ask them for help? "
                         "(yes OR no)", "yes", "no")
        if quizzes == "yes":
            print_pause("They strange man asks you the following "
                        "three questions:")
            player[6] = quiz("1) I am orange and sound like a parrot. "
                             "I am a __________", "carrot", "Behemoth Mace")
            player[7] = quiz("\n2) what goes up but never comes "
                             "down?", "age", "Hulk Potion")
            player[5] = quiz("\n3) I have cities, but no houses. I "
                             "have mountains, but no trees. I have water, "
                             "but no fish. "
                             "I am a _______?", 'map', "Enigma Cracker")
        else:
            print_pause("\nYou decide to continue on your journey to escape")

    if player[5] == "Enigma Cracker" and player[4] is False:
        print_pause("\n Ohhh no!!")
        print_pause("Because you have no clothes on, you are "
                    "unable to equip the Enigma Cracker")
        print_pause("Reluctantly you drop the Enigma Cracker\n")
        player[5] = ""
    return player


def encounter(player, villain):
    '''
    The player meets with their 'best friend' for the first time and
    meets the villian for the first time also
    '''
    print_pause("As you continue searching the town you see a shadow "
                "swoop by")
    print_quick("Another shadow passes by")
    print_quick("Suddenly you see multiple shadows pass by, from "
                "the corner of you eyes")
    print_pause(f"You turn around only to find {player[8]} "
                "standing behind you")
    print_pause("With a sigh of relief you hug them\n")
    if player[4] is False:
        print_pause(f"{player[8]} asks you, why are you not wearing "
                    "any clothes?")
        print_pause("You tell them it's a long story")
    print_pause("You begin to fill your friend in on everything that's "
                "happened to you so far")
    print_pause("They then tell you that it's been months since they "
                "last saw you")
    print_pause("Stunned you ask them 'what exactly is going on?'")
    print_pause("\nThey tell you the story of how a portion of Earth was "
                "pulled into the Phantasm Void")
    print_quick("They then tell you that ruler of this place is "
                f"{villain[0]} {villain[2]}")
    print_quick("Shoked at what they said you ask them for picture of "
                f"{villain[0]}")
    print_pause("They show you the folliwng:\n")
    monsters(villain[2])
    print_pause("\nTaken aback, you ask if anyone's been able to escape?")
    print_quick("They tell you that they know of a way and "
                "start leading you towards that direction")
    print_quickest("~\n" * 3)
    print_quick(f"As you continue to follow {player[8]}, you realise "
                "you've been down this way before")
    print_pause("Finally you reach your destination; it's your house!\n")
    print_quick(f"Surprised, you turn to ask {player[8]} what's going on?")
    print_quick("Only to see their eyes glazed over as their body "
                "melts into a puddle of goop")
    print_quick(f"They form back up as a {villain[1]} version of yourself")
    print_quick("They then shout:")
    print_quick(f"\nAs promised I've brought {player[0]} to you!!".upper())
    print_quick("Let my family go, our deal is done!".upper())
    print_quicker("\nYou try to run, but it's too late, you're surrounded")
    print_quicker(f"All around you, you see many versions of {player[2]}")
    monsters(player[2])
    print_quicker("You look up")
    print_quicker(f"You see {villain[0]} {villain[2]} coming down from the "
                  "sky and landing on top of your topsy-turvy house")
    print_quickest("Panicking, you worry about what's going to happen "
                   "to you")
    print_quickest("You see a door on the side of the house, that "
                   "looks to have a keypad")
    player[11] = choice("Do you choose to fight OR run?", "fight", "run")

    return player


def code(text, player, villain):
    """
    Gives the user 3 attempts on typing in the code
    """
    valid = False
    retry = 0
    print_quick(text)
    while valid is False:
        chosen = input(f"You have {3-retry} attempt(s) remaining:\n...")
        if chosen == player[9]:
            print_quicker("Well done!!")
            if player[5] == "":  # if they guessed it
                print_quicker("Now that was a lucky guess!!")
            print_quicker("You've got the code right!!")
            print_quicker(f"You managed to escape from {villain[2]}")
            monsters(villain[2])
            print_quick("\nThey scream in frustration as they charge "
                        "towards you")
            print_quick("You laugh in their face as the door bolts "
                        "shut after you entered in")
            print_quicker("You hear a thump!")
            print_quicker(f"{villain[0]} {villain[2]} is banging "
                          "against the door, trying to break through")
            valid = True
            return "escaped"  # They managed to guess the code
        else:
            retry += 1

        if retry > 2:
            print_pause("\nSadly you failed to enter the correct code")
            print_pause(f"You must now face {villain[2]}")
            print_pause(f"{villain[0]} {villain[2]}, smiles a sly smile, "
                        "then laughs:\nMWAHAHAHAHA")
            monsters(villain[2])
            valid = True
            return ""  # This means they didn't enter the code correctly


def battle(player, villain):
    '''
    The battle begins
    The return statments happen for the lose conditions first
    The last return statment is for the win conditions
    '''
    if player[1] == "male":
        print_quick("\nYou decide to man up!")
    else:
        print_quick("\nYou decide to woman up!")
    print_quick(f"You turn to face {villain[0]} {villain[2]}")

    # 50% chance to win if they are missing one equipment
    win_lose = random.choice(["win", "lose"])

    if player[6] != "":
        if player[6] == "Sonic Shoes":
            print_quick("\nYou put on your Sonic Shoes")
            print_quick(f"You start dodging all the attacks of {villain[0]}")
            print_quick("You think to yourself, if only you had an opening, "
                        "you could gather enough speed to take them down")
            if player[7] == "" and win_lose == "win":
                print_pause("You decide not to worry about what "
                            "you don't have")
                print_quicker("You persevere and gain enough speed to get "
                              "behind them")
                print_quicker("With the momentum you gathered, you manage "
                              f"to get behind {villain[2]}")
                print_quicker("You push them toward the house")
            else:
                print_quicker("You frantically run towards "
                              f"{villain[0]} {villain[2]}")
                print_quicker("Sadly you weren't fast enough to face them")
                villain[3] = ""
                return villain
        elif player[6] == "Behemoth Mace":
            print_quick("\nYou equip your Behmoth Mace and ready yourself")
            print_quick("You start fighting back by parrying all the "
                        f"attacks of {villain[0]} {villain[2]}")
            print_quick("You think to yourself, if only you had enough "
                        "strenghth, you could to take them down in couple "
                        "of blows")
            if player[7] == "" and win_lose == "win":
                print_pause("You decide not to worry about what you "
                            "don't have")
                print_quicker("You persevere and slowly start pushing "
                              f"{villain[0]} {villain[2]} back")
                print_quicker("With determination alone, you manage "
                              "to gather enough stength to push them "
                              "toward the house")
            else:
                print_quicker(f"You frantically run towards {villain[2]}")
                print_quicker("Sadly you weren't fast enough to face them")
                villain[3] = ""
                return villain
    else:
        print_quick("Unfortunately you have no weapons equipped")

    if player[7] != "":
        print_quick(f"You decide to use the {player[7]}")
        if player[3] > 1:
            print_pause(f"If only you didn't snooze {player[3]} times, "
                        f"the {player[7]} would still be working")
            print_pause(f"You've decided to drop the {player[7]} and "
                        f"continue your battle with {villain[0]}")
            player[7] = ""
        else:
            print_quick("It worked!!")
            if player[7] == "Time Stopping Watch":
                print_quick("You activate the Time Stopping Watch")
                print_quicker("Everything starts slowing down")
                print_quicker("The world halts to a stop")
                print_quicker("With only 20 seconds left on the watch")
                print_quicker(f"You charge towards {villain[0]} {villain[2]}")
                if player[6] != "" or (player[6] == "" and win_lose == "win"):
                    print_quickest("You manage to get behind "
                                   f"{villain[0]} {villain[2]}")
                    print_quickest("You push them toward the house")
                else:
                    print_quicker(f"You frantically run towards {villain[0]}")
                    print_quicker("Sadly you weren't fast enough to face them")
                    villain[3] = ""
                    return villain

            elif player[7] == "Hulk Potion":
                print_quick("You drink the Hulk Potion")
                print_quicker("You feel somthing")
                print_quicker("You feel STRONGER!!")
                print_quicker(f"You charge towards {villain[0]} {villain[2]}")
                if player[6] != "" or (player[6] == "" and
                   win_lose == "win"):
                    print_quickest("You grab your Behemoth Mace")
                    print_quickest("With ROAR and a hard smack!")
                    print_quickest("You start beating into "
                                   f"{villain[0]} {villain[2]}")
                else:
                    print_quicker("You fight frantically in your "
                                  "strengthened form")
                    print_quicker("Sadly your strength was not enough to "
                                  f"face {villain[0]} {villain[2]}")
                    villain[3] = ""
                    return villain

    if player[6] == player[7]:  # meaning they both are "" (empty)
        print_quick("Sadly you have no weapons or items to help you "
                    "in your battle")
        print_quick(f"You try and talk it out with {villain[0]} {villain[2]}")
        print_quick("Sadly it didn't work.")
        villain[3] = ""
        return villain

    # when refactoring, I realised this shows four times in
    # the win conditions (basically saved 24 lines)
    print_quickest("WHAM")
    print_quickest("WHAM")
    print_quickest("BAM")
    print_quicker("You've done it!!")
    print_quicker(f"You defeated {villain[0]} {villain[2]}, "
                  "by bashing them through the house")
    villain[3] = "defeated"
    return villain


def door(player, villain):
    print_quick("\nYou've chosen to flee for the door")
    print_quick("You come across a code panel")
    if player[5] == "":
        print_quick("Unfortunately, you don't have the Enigma Cracker "
                    "equipped to crack the code")
    else:
        print_quick("The Enigma Cracker gives you a hint to the "
                    f"{len(player[9])} digit code")
        print_quick("The code is equal to the time you woke up today:")
    villain[3] = code("You attempt to enter the code:", player, villain)
    if villain[3] == "":
        villain = battle(player, villain)
        return villain
    else:
        return villain


def the_story(player):
    today = datetime.datetime.now()
    t_day = today.day
    t_month = today.month
    t_year = today.year
    t_hour = today.hour
    t_mins = today.minute
    awake = "no"
    player[3] = 0  # if they play again this would need to reset to 0

    # And so it begins
    print_quick("\nQuickly you run to the portal before it closes")
    print_quick("You made it!!")
    print_quick(f"Just as you pass through you see {player[8]} "
                f"been pulled into the Phantasm Void by {player[2]}.")
    print_quicker(f"You scream {player[8].upper()}!!")

    print_quickest("\nBRRRRR....")
    print_quicker("BRRRRRRR....BRRRRRRRR")
    print_pause("*YAWN*")
    print_pause("\nYou wake up, unsure what day it is")
    print_pause(f"You check you phone and see it's {t_day}/{t_month}/{t_year}")
    print_pause(f"The time is {t_hour}:{t_mins}")
    while awake == "no":  # Notice how I don't mention the date again ;)
        awake = choice("Do you want to get out of bed? "
                       "(yes OR no)", "yes", "no")
        if awake == "no":
            print_pause("You choose to snooze your alarm")
            print_quick("\nBRRRRRRR....BRRRRRRRR")
            rand_mins = random.randint(1, 20)
            rand_hour = random.randint(0, 1)
            # This way if the mins go past 60 it add an extra hour
            if ((t_mins + rand_mins) % 60) != (t_mins + rand_mins):
                t_mins = (t_mins + rand_mins) % 60
                t_hour += 1
            else:
                t_mins = (t_mins + rand_mins) % 60
            t_hour = (t_hour + rand_hour) % 24
            print_pause(f"The time is {t_hour}:{t_mins}")
            player[3] += 1

    # this will be a code allowing the user to escape
    player[9] = f"{t_hour}{t_mins}"

    if player[3] > 1:
        print_pause(f"\nAfter snoozing the alarm {player[3]} times, you "
                    f"finally wake up at {t_hour}:{t_mins}")
    else:
        print_pause("\nYou're finally up!")
    print_pause("After going to the bathrom and having your shower, "
                "you realise today is going to be a hot day")
    clothes = choice("Would you like to wear some clothes? "
                     "(yes OR no)", "yes", "no")

    if clothes == "no":
        print_pause("\nYou've decided to go wild and strut in the nude\n")
        player[4] = False
    else:  # This is where the gender comes into play
        player[4] = True
        if player[1] == "male":
            print_pause("\nYou pick you favourite top and jogging bottoms "
                        "to wear\n")
        else:
            print_pause("\nYou picked your favourite top and shorts to wear\n")

    print_pause("Just as you sit down to check what's happening on "
                "social media")
    print_pause("You hear a loud crash and the room starts shaking")
    print_pause("Afraid that your house would crumble on top of you")
    print_pause("You step outside to see just what's happening")
    print_pause("To your surprise, you realise you're "
                "not actually on Earth\n")
    print_pause("Everything around you is the wrong way around (O_o)")
    print_pause("Cats are as tall as trees")
    print_pause("Birds are tunelling from the ground up")
    print_pause("Trees are falling from the sky, with the weight of a "
                "pillow...only to disappear once they touch the ground\n")
    print_pause("After taking in your surroundings")
    print_pause("You've resolved yourself to finding your way back "
                "home and start to walk out of the cul-de-sac")
    print_pause("You are met with a fork in the road")
    player[10] = choice("Do you want to go left OR right?", "left", "right")
    return player


def user():
    '''
    player list:
    [0] = name
    [1] = gender
    [2] = fear
    [3] = snoozed
    [4] = clothes
    [5] = Enigma Cracker
    [6] = weapon 1
    [7] = weapon 2
    [8] = best friend
    [9] = code
    [10] = fork in the road
    [11] = fight of flight
    [12] = Play
    [13] = Play again count
    '''
    player = ["", "", "",
              0, False, "",
              "", "", "", "",
              "", "", "", 0]
    player[0] = input(" - What's your name:\n...")
    if player[0] == "":  # in case they just press enter
        player[0] = "Player"
    player[8] = input("\n - What's your best friend's name:\n...")
    if player[0] == "":
        player[0] = "Bestie"
    player[1] = choice("\n - Are you male OR female?", "male", "female")
    player[2] = input("\n - What are you afraid of?\n...")
    # If no input it regsiters as 'the Nothingness Paradox',
    # which would also make an intersting story
    if player[2] == "":
        player[2] = "the Nothingness Paradox"
    return player


def bad_guy(player):
    '''
    villain list:
    [0] = name
    [1] = gender
    [2] = type
    [3] = defeated OR escaped
    '''
    villain = ["", "", "", "", ""]
    # Slicing the name to create a mirror copy
    villain[0] = (player[0][len(player[0])::-1]).lower()
    # Capitalize the first letter
    villain[0] = villain[0][0].upper() + villain[0][1:len(villain[0])]
    if len(villain[0]) > 4:  # adding some umph to the villain's name
        villain[0] = villain[0][0:2] + "-" + villain[0][2:len(villain[0])]

    if player[1] == "male":
        villain[1] = "female"
    else:
        villain[1] = "male"

    chosen = random.randint(0, 7)
    monster_types = ["the Goblin King", "the Broken Clown", "the Hydra Spider",
                     "the ArGru Conqueror", "the Upside-down Teletubby",
                     "the Circle of oOoOo", "Death's Cousin",
                     " the Shark with Gummy Bear teeth"]
    monster_types.append(player[2])
    villain[2] = monster_types[chosen]

    return villain


def lets_play():
    '''
    Main funcion
    '''
    # Calling all variables required
    print_pause("\n Welcome to your Story")
    print_pause("\nA few house rules:")
    print_pause("   1) When a prompt is required the console will display "
                "'...' in front of an empty line")
    print_pause("   2) Answers are accepted in a single work "
                "e.g. yes, no, open etc.")
    print_pause("   3) Once you've entered an answer"
                ", press the 'ENTER' or 'RETURN' key\n")
    print_pause("Before we begin, could you tell us:")

    # Made them both as lists so that I can return the details required
    player = user()
    villain = bad_guy(player)

    # The game starts from here
    player[12] = choice("\nAre you ready to begin?(yes OR no)", "yes", "no")
    player[13] = 0
    start_time = time()

    while player[12] == "yes":
        player = the_story(player)
        player = middle(player)
        player = encounter(player, villain)
        if player[11] == "fight":
            villain = battle(player, villain)
        if player[11] == "run":
            villain = door(player, villain)
        player = ending(player, villain)
        player[13] += 1

    end_time = time()
    # Calculates the total amount of time taken
    total_time = end_time - start_time
    # 3600 seconds in 1 t_hour
    t_hours = int(total_time / 3600)
    # remainder to calculate minutes and seconds
    t_hourless = total_time % 3600
    # 60 seconds in a minute
    minutes = int(t_hourless / 60)
    # what's left will equal seconds
    seconds = round(t_hourless % 60)

    if villain[3] != "":  # Player wins
        print_pause("\nWell done!!"
                    f"\nYou completed {player[13]} game run(s) in - "
                    f"{t_hours}h:{minutes}m:{seconds}s")
    else:  # Player loses
        print_pause("\nBetter luck next time!"
                    f"\nYou lasted - {t_hours}h:{minutes}m:{seconds}s")


lets_play()
