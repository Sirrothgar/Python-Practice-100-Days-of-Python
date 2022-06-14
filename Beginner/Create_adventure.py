print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Write your code below this line 👇
road = input("You travel down the raod and come to a crossroad. Where do you want to go? Type 'left' or 'right' ").lower()

if road == "left":
    lake = input("The road continues down to a lake where you see a island in the middle. Do you wait for a boat or swim across? Type 'Swim' or 'Wait'").lower()
    if lake == "wait":
        door = input("A boat falls out of the sky into the water to let you across.When you get to the island, "
                     "there is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?").lower()
        if door == "yellow":
            print("You choose the right door and are safe. Congratulations, you won!")
        elif door == "red":
            print("Fire shoots out of the door and you melt to death. Game over.")
        elif door == "blue":
            print("A tidal wave comes through the door and pushes you into the lake where you drown because you can't swim. Game over.")
        else:
            print("There is no door with that color, you're trying to cheat and I don't like cheaters so game over!")
    elif lake == "swim":
        print("You forgot you don't know how to swim and drown. Game over.")
    else:
        print("That wasn't an option, I'm sorry but game over.")
elif road == "right":
    print("You didn't look good enough and fell into a bottomless pit. Game over.")
else:
    print("You don't have a delorean to go in any other direction. Game over")
