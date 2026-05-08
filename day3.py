print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
answer1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" \n').lower()
if answer1 == "left":
    answer2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if answer2 == "wait":
        answer3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if answer3 == "red":
            print("It\'s a room full of fire. Game Over.")
        elif answer3 == "yellow":
            print("You found the treasure! You Win!")
        elif answer3 == "blue":
            print("You enter a room with a dragon. Game Over.")
        else:
            print("You chose a door that doesn\'t exist. Game Over.")
    else:
        print("You get attacked by a shark. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    