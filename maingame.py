import playercharactercreation
import gameresources
import random
import time

def playagain():
    print("Do you want to play again?")
    player_answer = input("(y/n)>").lower()
    if "y" in player_answer:
        start_adventure()
    if "n" in player_answer:
        exit()
 
def red_room():
    enemy_list = list(gameresources.enemydict.keys())
    random_enemy_index = random.randint(0, 3)
    enemyencountered = enemy_list[random_enemy_index]
    enemystats = list(gameresources.enemydict.get(enemyencountered))
    playerclass = list(gameresources.playerdict.values())
    player_stats = list(gameresources.classdict.get(playerclass[0]))
    print(f"You see a {enemyencountered} guarding a chest.\n What do you do?")
    print(f"1: Fight the {enemyencountered}. \n2: Flee")
    player_answer = int(input(">"))
    if player_answer == 1:
        print(f"You start fighting the {enemyencountered}.")
        if player_stats[3] >= enemystats[3]: #player has advantage
            print("You take the advantage!")
            x = 0
            while enemystats[0] > 0:
                pdamage = (player_stats[1] - enemystats[2])
                enemystats[0] -= pdamage
                print(f"You deal {pdamage} damage to the {enemyencountered}.")
                time.sleep(1)
                edamage = (enemystats[1] - player_stats[2])
                player_stats[0] -= edamage
                time.sleep(1)
                print(f"You take {edamage} damage from the {enemyencountered}")
                if enemystats[0] <= 0:
                    print(f"You defeat the {enemyencountered}!")
                    print("Do you want to open the chest?")
                    player_answer = input("(y/n)>").lower()
                    if player_answer == "y":
                        print("You open the chest and find golds. Thus you return home to live a life of prosperity...")
                        exit()
                    elif player_answer == "n":
                        print("You turn your back on the chest hoping to find treasure elsewhere but you find none...this mishap makes you only more determined than before.")
                        exit()
                elif player_stats[0] <= 0:
                    print("You were defeated!")
                    exit()
            x += 1 
        elif player_stats[3] < enemystats[3]:
            print("You are at an disadvantage!")
            x = 0
            while enemystats[0] > 0:
                edamage = (enemystats[1] - player_stats[2])
                print(f"You take {edamage} damage from {enemyencountered}.")
                time.sleep(1)
                player_stats[0] -= (enemystats[1] - player_stats[2])
                pdamage = (player_stats[1] - enemystats[2])
                enemystats[0] -= (player_stats[1] - enemystats[2])
                print(f"You deal {pdamage} damage to {enemyencountered}.")
                time.sleep(1)
                if enemystats[0] <= 0:
                    print(f"You defeat the {enemyencountered}!")
                    print("Do you want to open the chest?")
                    player_answer = input("(y/n)>").lower()
                    if player_answer == "y":
                        print("You open the chest and find golds. Thus you return home to live a life of prosperity...")
                        exit()
                    elif player_answer == "n":
                        print("You turn your back on the chest hoping to find treasure elsewhere but you find none...this mishap makes you only more determined than before.")
                        exit()
                elif player_stats[0] <= 0:
                    print("You were defeated!")
                    exit()
                x += 1

     
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