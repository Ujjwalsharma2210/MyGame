###############################################
#                                             #
#       Author UjjwalSharma 19/11/2020        #
#               Version 1.5                   #
#               							  #
###############################################

# NOTE: add player health points(HP)
# NOTE: add bats that reduce player's health points
# NOTE: add sense of direction(player knows where he is and where to go)

import random as rand

# import time

# ----GLOBAL----
positionOfKeys = []

currentPositionOfPlayer = ()

# For round 2
positionOfSword = ()
positionOfDemon = ()

# Size of grid
max = 2
min = -max

# Initial position of player
x, y = 0, 0

# State of the game : Running or not
gameRunning = True

# Tells if the current position is a corner or not
isCorner = False
# Tells if the current position is an edge or not
isEdge = False

# number of keys
numberOfKeys = 3

# tracks the number of keys found
keyCount = 0


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

def spawnDemonAndSword():
	pass


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
		print("Wrong move! Use a, w, s and d to move around")

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
	else:
		isCorner = False

	return isCorner


def checkForEdge(playerCurrentPosition):
	global max, min
	global isCorner, isEdge

	x, y = playerCurrentPosition

	if not isCorner:
		if x == max:
			print("\nYou are at the right edge")
			isCorner = True
		elif x == min:
			print("\nYou are at left edge")
			isCorner = True
		elif y == max:
			print("\nYou are at top edge")
			isCorner = True
		elif y == min:
			print("\nYou are at bottom edge")
			isCorner = True
		else:
			isCorner = False

	return checkForEdge


def checkPlayerPosition(playerCurrentPosition):
	# Checks if the player has reached a corner and prints the output
	checkForCorner(playerCurrentPosition)

	# Checks if the player has reached an edge and prints the output
	checkForEdge(playerCurrentPosition)


# NOTE: Figure out how to make multiple rounds


# Checks if a key was found.
def isKeyFound(playerPosition, keysPosition):
	global keyCount

	for element in keysPosition:
		if element == playerPosition:
			print("A KEY WAS FOUND!!!!")
			keyCount += 1


# Runs when all the keys have been found and initiates next round
def allKeysFound(keyCount):

	allFound = False

	if checkKeys(keyCount):
		allFound = True

	return allFound


def finalRound():

	global keyCount
	global positionOfSword
	global positionOfDemon
	global x, y
	x, y = 0, 0

	keyCount = 0
	print("Final Round Started.")

	spawnDemonAndSword()

	while gameRunning:
		playerPosition = makeMove()



# If the player finds the demon first, player dies and game ends
# NOTE: Complete finalRound()


# Runs the game
def playGame():
	global positionOfKeys, keyCount

	print("To wander around in this world\n"
	      "Type up, down, right or left\n"
	      "Start roaming and explore !!!\n")

	# NOTE : Remove next line
	print(keys)

	# Check
	while gameRunning:
		# playerPosition temporarily saves the position of the player
		playerPosition = makeMove()

		# To check if the player has reached an edge or a corner
		checkPlayerPosition(playerPosition)

		isKeyFound(playerPosition, positionOfKeys)

		# Checks and tells the player if all the keys have been found
		if allKeysFound(keyCount):
			print("ALL THE KEYS HAVE BEEN FOUND!!")
			print("Now you are worthy of finding the sword.")
			print("If you meet ZAARU before finding the sword you will die!")
			finalRound()
			break
		else:
			continue


# main function Which asks to start the game
def startGame():
	# Input player name and print welcome sentence
	playerName = str(input("\nHello wanderer! What's your name?\n"))

	print("\nHello " + playerName + ", Welcome to the world of blocks!\n"
	      "This world is cursed by the demon king ZAARU, You are sent here to save us\n"
          "You can move around by using w, a, s, d to go up, left, down and right respectively.\n"
          "Collect the keys keys to go second round\n"
		  "Find the sword first to kill ZAARU.\n"
          "Are you ready for the adventure?\n"
          "If you get lost you will not be able to find your way again.")

	print()

	initiation = input("Enter y or n : ")
	if initiation == "y":
		playGame()
	elif initiation == "n":
		print("Come prepared next time!\n"
		      "We need you")
		exit()


startGame()
