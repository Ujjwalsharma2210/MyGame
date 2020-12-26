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


# Everytime the player makes a move this function return values of x and y
def makeMove():

    global x
    global y
    # Increment and decrement x and y as per input
    move = input("Move to : ")
    if move == "up":
        y += 1
    elif move == "down":
        y -= 1
    elif move == "right":
        x += 1
    elif move == "left":
        x -= 1
    else:
        print("Wrong move! Type right, left, up or down.")

    return x, y


keys = spawnKeys()


def checkKeys(numberOfKeys):

    global keys

    if numberOfKeys == len(keys):
        print("ALL THE KEYS HAVE BEEN FOUND")


def checkPlayerPosition(playerCoordinates):
    global currentPositionOfPlayer


# Runs the game
def startGame():
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

        checkKeys(keyCount)


# main function Which asks to start the game
def playGame():
    # Input player name and print welcome sentence
    playerName = input("\nHello wanderer! What's your name?\n")
    print()
    print("Hello " + playerName + ", Welcome to the world of blocks!\n"
          "This world is cursed by the demon king ZAARU, You are sent here to save us\n"
          "You can type where you want to go like up, down, right or left.\n"
          "Collect the keys and find the sword first to kill ZAARU.\n"
          "Are you ready for the adventure?")
    print()
    initiation = input("Enter y or n : ")
    if initiation == "y":
        startGame()
    elif initiation == "n":
        print("Come prepared next time!\n"
              "We need you")
        exit()


playGame()
