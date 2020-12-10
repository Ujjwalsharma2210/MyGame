def startGame():
    pass


# main function
def mainFunction():
    
    playerName = input(print("Hello wanderer! What's your name?"))
    print("Hello " + playerName + ", Welcome to the world of blocks!"
          "This world is cursed by the demon king ZAARU, You are sent here to save us\n"
          "The person who comes here can only move up, down, right or left by making a wish.\n"
          "Collect the keys and open doors to find relics which will help you to defeat the demon...\n"
          "Are you ready for the adventure?")
    initiation = input("Enter y or n : ")
    if initiation == "y":
        startGame()

mainFunction()
