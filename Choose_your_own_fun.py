print("Welcome to the game of your choice!")

name = input("What is your name? ")
print("Welcome", name,  "to the game of adventure!")

answer = input("Your are on a dirb road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a lake, there is an island in the middle of the lake. Type walk to walk are swim to swin.? ").lower()
    if answer == "swim":
        print("You were eaten by a shark. Game over.")
    elif answer == "walk":
        print("you walk so many miles and you are tired and ran out of water. Game over.")
    else:
        print("Not a valid option. You lost.")
        



elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or go back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and you are loss the way. Game over.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold and tell you the way to the home. You won!")
        elif answer == "no":
            print("You ignore the stranger and they are angry and you lost the way. Game over.")

else:
    print("Not a valid option. You lost.")