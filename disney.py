print('''
                                     |
                 ||                // \\                     Disneyland's
                 ==             / /     \ \                  Haunted Mansion
                 ==          =================
                 ==          |   |   _   |   |
                 ==          |() |  (_)  | ()|
             |=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
--------------|    ___           __--^--__          ___     |
|             |  [[_|_]]     __--   ___   --__    [[_|_]]   |
|             |  [[_|_]] __--      /   \     --__ [[_|_]]   |
|  =====================================================================
====||_/\_||_/\_||_/\_|| |=======================| ||_/\_||_/\_||_/\_||
 |  ||    ||    ||    || ***    ***     ***    *** ||    ||    ||    ||
 |  ||    ||    ||    || ***    ***_/^\_***    *** ||    ||    ||    ||
 |  ||    ||    ||    || ***    ***|   |***    *** ||    ||    ||    ||
 |  ||++++||++++||++++|| ***----***-----***----*** ||++++||++++||++++||
 |==||====||====||====||_***====***=====***====***_||====||====||====||
 |  ||_/\_||_/\_||_/\_|| ***    ***     ***    *** ||_/\_||_/\_||_/\_||
 |  ||    ||    ||    || ***    ***_____***    *** ||    ||    ||    ||
 |  ||    ||    ||    || ***    ***|   |***    *** ||    ||    ||    ||
 |  ||    ||    ||    || ***    ***|  o|***    *** ||    ||    ||    ||
 |  ||++++||++++||++++|| ***----***-----***----*** ||++++||++++||++++||
 |==||====||====||====||_***====***=====***====***_||====||====||====||
==============================================================================
''')
print("Welcome to the Disneyland Haunted Mansion")
print("Your mission is to survive in this Haunted Mansion")
choice1=input('You\'ve a path split. Type "left" or "right" to choose your way.\n').lower()
if choice1 == "right":
  choice2 = input('You\'ve escape from the zombies. There is "pepsi" and "burger" on the table. Type what you want to eat?\n').lower()
  if choice2=="burger":
    choice3=input('That burger gave you energy. Suddenly,"fairy" and "beast" appeared infront of you. Type who would you like to be friends with?\n').lower()
    if choice3 == "beast":
      print("The beast turned into a charming prince. He led you to the exit door. Congratulations you survived unharmed.\n")
    else:
      print("Game Over.The fairy turned into a black witch and killed you\n")
  else:
    print("Game Over.Pepsi had poison in it and you died.\n")
else:
  print("Game Over.Angry trout attacked you and you died.\n")
