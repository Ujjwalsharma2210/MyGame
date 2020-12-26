import random as rand

positionOfKeys = []
gameRunning = True
x = y = 0
#
# # Returns True if one of the input values is 0
# # and returns False if none of the values is 0
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

    # Local variables
    numberOfKeys = 3

    minvalue = -3
    maxvalue = 3

    # Loop to generate and add number of keys
    for numberOfKeys in range(0, numberOfKeys):
        x = rand.randint(minvalue, maxvalue)
        y = rand.randint(minvalue, maxvalue)

        # Checks if one of the values is zero.
        while x == 0 or y == 0:
            if oneIsZero(x, y):
                x = rand.randint(minvalue, maxvalue)
                y = rand.randint(minvalue, maxvalue)

        positionOfKeys.append((x, y))

    print(positionOfKeys)


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

#
# spawnKeys()
def startGame():
    print("To wander around in this world\n"
          "Type up, down, right or left\n"
          "Start roaming and explore !!!\n")

    keys = spawnKeys()
    while gameRunning:
        if (makeMove()) in keys:
            print("A KEY was found")

startGame()
# def printGrid(val):
#     # The grid will always be square
#     # This grid will show the position of the spawned keys of the level
#     gird = []
#     # -x, y -> x++
#     #   |
#     #   V
#     #  y--
#
#     # Creating grid using above logic
#     for x in range(-val, val+1):
#         for y in range(val, -(val-1)):
#             print((i, j))
#             val -= 1
#         print()
#         val += 1
#
# printGrid(2)
