"""
The Main File for my Integration Project
"""
___author___ = "Payton Bryant"


# Choose Your Own Adventure - Dungeon Edition; in this program you will
# be able to choose certain options to hopefully make it through to the end
# the dungeon


# Left Room Functions
def left_room(left):
    """
    Displays the dialogue for the left room choice
    :param left:
    :return:
    """
    print(left)
    print("Your only route from this room is to go down the trapdoor."'\n')
    print(
        "You go down the ladder to find yourself in a small cave with a "
        "lagoon on one side of it."'\n')
    print("You go towards it to see gurgling in the water."'\n')
    print("A humanoid frog jumps out and is ready to attack!"'\n')
    return


def frog_sword_battle():
    """
    Displays the dialogue for choosing sword in the frog battle
    :return:
    """
    print(
        "You use your sword and do 6 damage to the frog. It also does 6 "
        "damage to you."'\n')
    print("You do 5 damage to the frog. The frog does 4 damage to you."'\n')
    print("You have died. Thanks for playing!")
    return


def frog_vial_battle():
    """
    Displays the dialogue for choosing vial in the frog battle
    :return:
    """
    print(
        "You throw the contents of the vial onto the frog and it starts "
        "burning."'\n')
    print(
        "It runs to a corner to deal with it's pain. In it's absence you see "
        "a cave with light coming through it in the lagoon."'\n')
    print(
        "You jump into the lagoon and go through the cave and come out on"
        " a cliffside."'\n')
    print("Congratulations! You won.", sep='')
    return


def frog_bone_battle():
    """
    Displays the dialogue for choosing bone in the frog battle
    :return:
    """
    print(
        "You throw the bone across the room hoping the frog will chase it."
        '\n')
    print(
        "The frog looks at you with disdain and lunges at you doing 10 damage."
        '\n')
    print("You have died. Thank you for playing!")
    return


# Right Room Functions
def right_room(right):
    """
    Displays the dialogue for the right room choice
    :param right:
    :return:
    """
    print(right)
    print(
        "The mass starts to move and you can start to recognize that it is "
        "a giant bear."'\n')
    print("It starts to make its way to you and seems aggressive."'\n')
    print("Before it can attack you, you use your weapon." '\n')
    return


def bear_sword_battle():
    """
    Displays the dialogue for choosing sword in the bear battle
    :return:
    """
    health = 10
    print(
        "You use your sword and do 6 damage! You take 3 damage from the bear "
        "scratching you with its claws. Your current health: ")
    health -= 3
    print(health, '\n')
    print(
        "You did 7 damage! You take another 3 damage from the bear's claws. "
        "Your current health: ")
    health -= 3
    print(health, '\n')
    print(
        "You do a final 6 damage and kill the bear! You see an opening in one "
        "of the walls as light is pouring through." '\n')
    print("You run through the opening and make it out onto a cliffside."'\n')
    print("Congratulations! You won.", sep='')
    return


def bear_vial_battle():
    """
    Displays the dialogue for choosing vial in the bear battle
    :return:
    """
    print(
        "You throw the contents of the vial onto the bear and it seemed to "
        "enjoy it?"'\n')
    print(
        "In it's happy endeavor, it accidentally swipes viciously at you and "
        "kills you."'\n')
    print("The end. Thank you for playing!")
    return


def bear_bone_battle():
    """
    Displays the dialogue for choosing bone in the bear battle
    :return:
    """
    print("You hold the bone out for the bear to sniff."'\n')
    print(
        "It mistakes your arm for the bone you just offered and bites your "
        "arm."'\n')
    print("It viciously yanks your arm off and you end up bleeding out."'\n')
    print("The end. Thank you for playing!")
    return


# Introduction
def main():
    """
    Main includes the introduction, weapon choice, and room choice options
    """
    print("Hello, new player! What is your name?")
    name = input("Name: ")
    print("Welcome, " + name, '\n')
    # I used Quora to read how to put spaces between lines of code

    # Weapon choice
    print(
        "You find yourself waking up in the middle of a dank, vast dungeon."
        '\n')
    print(
        "You look around to find three items: a sword, a vial with liquid of "
        "some sort in it, and a bone."'\n')
    print("What would you like to bring with you?" '\n')

    # Variables for Weapons
    weapon_choice = (input())
    sword = "Logical decision."'\n'
    vial = "I see you like the weird things."'\n'
    bone = "What? You think you're going to tame a dog with that?"'\n'
    # TA helped me with putting quotes around the variable names
    if weapon_choice == "sword":
        print(sword)
    elif weapon_choice == "vial":
        print(vial)
    elif weapon_choice == "bone":
        print(bone)
    else:
        print("Exit and retry.")
        exit()

    # First battle choice
    print(
        "Now that you have picked a weapon (maybe?), time to venture forth "
        "into the darkness."'\n')
    print(
        "You walk down a hallway with skulls and cobwebs littering the walls."
        '\n')
    print(
        "To your left, you see an empty cell with a trapdoor in the floor in "
        "the corner of the room."'\n')
    print(
        "On your right, you see a very open cave-like room with various body "
        "parts on the ground."'\n')
    print("Which way would you like to go?"'\n')
    room_choice = (input())

    # Rooms
    left = "You go into the room with hay all over the floor and a skeleton " \
           "hanging from chains on the wall."'\n'
    right = "You head into the cave and notice a giant dark mass in the " \
            "corner."'\n'

    # Left Room (cell) choice
    if room_choice == "left":
        left_room(left)
        if weapon_choice == "sword":
            frog_sword_battle()
        elif weapon_choice == "vial":
            frog_vial_battle()
        elif weapon_choice == "bone":
            frog_bone_battle()

    # Right Room (cave) choice
    elif room_choice == "right":
        if weapon_choice == "sword":
            bear_sword_battle()
        elif weapon_choice == "vial":
            bear_vial_battle()
        elif weapon_choice == "bone":
            bear_bone_battle()
    else:
        print("Exit and retry.")
        exit()


# CALL TO MAIN #
main()
