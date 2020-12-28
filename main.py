###############################################
#                                             #
#       Author UjjwalSharma 19/11/2020        #
#               Version 1.4                   #
#               							  #
###############################################

import random as rand
# import time

# ----GLOBAL----
positionOfKeys = []

currentPositionOfPlayer = ()

# Size of grid
max = 2
min = -max

# Initial position of player
x = y = 0

# State of the game : Running or not
gameRunning = True

# Tells if the current position is a corner or not
isCorner = False
# Tells if the current position is an edge or not
isEdge = False

# number of keys
numberOfKeys = 3


# Returns True if one of the input values is 0
# and returns False if none of the values is 0
def oneIsZero(x, y):
    if x == 0 or y == 0:
        return True
    else:
        return False


# Spawns keys at different random positions which need to be collected
# by the player to get to the next level
def spawnKeys():

    # Global variable to store the position of keys
    global positionOfKeys
    global min
    global max

    # Local variables
    global numberOfKeys

    # Loop to generate and add number of keys
    for numberOfKeys in range(0, numberOfKeys):
        x = rand.randint(min, max)
        y = rand.randint(min, max)

        # Checks if one of the values is zero.
        while x == 0 or y == 0:
            if oneIsZero(x, y):
                x = rand.randint(min, max)
                y = rand.randint(min, max)

        positionOfKeys.append((x, y))

    return positionOfKeys


keys = spawnKeys()


# Everytime the player makes a move this function return values of x and y
def makeMove():

    global x
    global y
    # Increment and decrement x and y as per input
    move = input("Move to : ")
    if move == "w":
        y += 1
    elif move == "s":
        y -= 1
    elif move == "d":
        x += 1
    elif move == "a":
        x -= 1
    else:
        print("Wrong move! Type right, left, up or down.")

    return x, y


def checkKeys(numberOfKeys):

    global keys
    allFound = False

    if numberOfKeys == len(keys):
        allFound = True

    return allFound


def checkForCorner(playerCurrentPosition):

    global max, min
    global isCorner

    x, y = playerCurrentPosition
    if x == max and y == max:
        print("You have reached upper right corner")
        isCorner = True
    elif x == max and y == min:
        print("You have reached lower right corner")
        isCorner = True
    elif x == min and y == max:
        print("You have reached upper left corner")
        isCorner = True
    elif x == min and y == min:
        print("You have reached lower left corner")
        isCorner = True

    return isCorner


def checkForEdge(playerCurrentPosition):

    global max, min
    global isCorner, isEdge

    x, y = playerCurrentPosition

    if not isCorner:
        if x == max:
            print("You are at the right edge")
        elif x == min:
            print("You are at left edge")
        elif y == max:
            print("You are at top edge")
        elif y == min:
            print("You are at bottom edge")


def checkPlayerPosition(playerCurrentPosition):

    checkForCorner(playerCurrentPosition)

    checkForEdge(playerCurrentPosition)


def finalRound():
    # TODO: complete the second and final round
    pass


# Runs the game
def playGame():
    print("To wander around in this world\n"
          "Type up, down, right or left\n"
          "Start roaming and explore !!!\n")

    # increments when a key is found
    keyCount = 0

    global keys
    print(keys)

    # Main game loop
    while gameRunning:

        # playerPosition temporarily saves the position of the player
        playerPosition = makeMove()

        # To check if the player has reached an edge or a corner
        checkPlayerPosition(playerPosition)

        for element in keys:
            if element == playerPosition:
                print("A KEY WAS FOUND!!!!")
                keyCount += 1

        # Checks and tells the player if all the keys have been found
        if checkKeys(keyCount):
            print("ALL THE KEYS HAVE BEEN FOUND!!")
            print("Now you are worthy of finding the sword.")
            print("If you meet ZAARU before finding the sword you will die!")

            # Second round of the game.
            # Player has to find the sword before the demon to win
            # If the player finds the demon first, player dies and game ends
            finalRound()


# main function Which asks to start the game
def startGame():
    # Input player name and print welcome sentence
    playerName = input("\nHello wanderer! What's your name?\n")
    print()
    print("Hello " + playerName + ", Welcome to the world of blocks!\n"
          "This world is cursed by the demon king ZAARU, You are sent here to save us\n"
          "You can move around by using w, a, s, d to go up, left, down and right respectively.\n"
          "Collect the keys and find the sword first to kill ZAARU.\n"
          "Are you ready for the adventure?\n"
          "One more important thing, If you get lost you will not be able to find your way again.")
    print()
    initiation = input("Enter y or n : ")
    if initiation == "y":
        playGame()
    elif initiation == "n":
        print("Come prepared next time!\n"
              "We need you")
        exit()


startGame()
