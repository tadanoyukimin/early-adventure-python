import playercharactercreation

def playagain():
    print("Do you want to play again?")
    player_answer = input("(y/n)>").lower()
    if "y" in player_answer:
        start_adventure()
    if "n" in player_answer:
        exit()
 
def red_room():
    print("You see a skeleton guarding a chest.")
    print("What do you do?")
    print("1: Fight the skeleton.")
    print("2: Flee.")
    player_answer = int(input(">"))
    if player_answer == 1:
        print("You start fighting the skeleton.")
        print("You defeat the skeleton!")
        print("Do you want to open the chest?")
        player_answer = input("(y/n)>").lower()
        if player_answer == "y":
            print("You open the chest and find golds. Thus you return home to live a life of prosperity...")
            exit()
        elif player_answer == "n":
            print("You turn your back on the chest hoping to find treasure elsewhere but you find none...this mishap makes you only more determined than before.")
            exit()
    elif player_answer == 2:
        print("You are successful at fleeing. The adventure was over before it began...but that only makes you even more determined than before...")
        playagain()
    else:
        print("Please choose one of the options listed.")
        red_room()

def blue_room():
    print("There is nothing in this room.")
    print("Go back?")
    player_answer = input("(y/n)> ").lower()
    if "yes" in player_answer or "y" in player_answer:
        start_adventure()
    elif "no" in player_answer or "n" in player_answer:
        print("You stay in the room. The adventure was over before it began...but that only makes you even more determined than before... ")
        playagain()

def start_adventure():
    print("You see a red and blue door in front of you.")
    player_answer = input("Which door do you choose?> ")
    if str(player_answer.lower()) == 'red':
        red_room()
        return "You chose the red door."
    elif str(player_answer.lower()) == "blue":
        blue_room()
        return "You chose the blue door."
    else:
        "Please choose a door."
start_adventure()