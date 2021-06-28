import gameresources

print("Welcome to a textbased adventure based on Python! \n Please note, many things are still in development.")
player_name = input("Please enter your name: ")
gameresources.playerdict = {player_name: 0}
print(f"Your name is {player_name}.")
print("Please choose your class from the following:")
print("Knight: The knight has high health and defense.")
print("Spellcaster: The spellcaster has high attack but low defense.")
print("Ranger: The ranger has average attack and defense.")

while True:
    try:
        player_class = input("Please choose a class: ")
        player_class = player_class.title()
        errorcheckpc = str(player_class)
        if errorcheckpc in gameresources.classdict.keys():
            break
        else:
            raise Exception
    except Exception:
        print("Please choose a class from the list of classes: Knight, Spellcaster or Ranger.")

print(f"{player_name}, you are now a {player_class}!")
gameresources.playerdict[f"{player_name}"] = player_class
print(input("Enter Start to start your adventure!> "))

#make custom class later?