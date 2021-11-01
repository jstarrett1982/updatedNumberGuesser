# Number guessing game, version two
# By: Jackie Starrett
# This game stores the user name, allows the player to guess a number between 1 and 100, tells the player to guess higher or lower
# Once the player guesses the correct number, the player is notified, their score is evaluated against a list of top scores.
# The top five scores are displayed to the player.  If the player's score is in the top 5, it is printed with the other 4 top scores and stored.
# The player is given the option to play again.  The player can quit while playing the game.

# this imports a library that allows for random number generation
import random

# creating empty variables which will be added to.
secretNum = 0
numGuesses = 0
newScore = []


# creating the function for the game.
def playGame():
    # This function generates a random integer between 1 and 100 (inclusive), and assigns it to the variable secretNum.
    # we will add to the list later.  We then create a session to read the text file for the top five players.
    # each line of the text file is stripped down to two parts and stored in the list above.
    secretNum = random.randint(1, 100)
    topFiveList = []
    topReadingSession = open("topPlayers.txt", "r")
    for eachLine in topReadingSession.readlines():
        score = eachLine[0:9].rstrip()
        name = eachLine[10:40].rstrip()
        topFiveList.append([score, name])

    # the list of top players is sorted, ascending, by score.
    topFiveList.sort(key=lambda x: (int(x[0]), x[1]))

    # The reading session is closed
    topReadingSession.close()

    # This variable will get put into the loop and keep track of the number of guesses.
    numGuesses = 0

    # this asks the player for their name
    name = input("Please enter your name   ")
    print()

    # The gameStatus determines when the loop is over.
    gameStatus = 0

    while gameStatus == 0:
        # this asks the user to enter a number
        guess = input("guess a number between 1 and 100, Q quits   ")

        # Evaluates if the guess is a number
        if str.isnumeric(guess):

            # each time the game goes through the loop,one is added to number of guess
            numGuesses = numGuesses + 1

            # evaluates if guess is less than the secret number, then prints appropriate message.  The player returns to the beginning of the loop to guess again.
            if int(guess) < secretNum:
                print()
                print("your answer is LOWER than the secret number   ")
                print()

            # evaluates if guess is higher than the secret number, and gives appropriate response if it is.
            elif int(guess) > secretNum:
                print()
                print("your answer is HIGHER than the secret number   ")
                print()

            # this is triggered if the player guesses the correct answer, prints a response with their name and number of guesses.
            # the change in game status kicks the player ot of the loop.
            else:
                print()
                print("CONGRATULATIONS,", name, " you guessed the number in", numGuesses, "guesses")
                gameStatus = 1

        # if the player enter a string, specifically q or Q, the game ends and the change in game status knocks the player out of the loop
        elif guess.upper() == "Q":
            gameStatus = 2
            print("Looks like you are ready to quit.  Goodbye!")
            print()
            quit()

        # if the player enters any other string, this line is activated and the player is sent to the beginning of loop to start again.
        else:
            print()
            print("please enter a number,not a string")
            print()

    # this stores the player's name and score (number of guesses) in the newScore variable
    newScore = [numGuesses, name]

    # This loop reads through each line of the topFiveList and evaluates if the score is less than the player's new score.
    # If the player's score is less than any of the scores on the list, the last (highest) score is popped off the list.
    for i in range(0, len(topFiveList)):

        if int(topFiveList[i][0]) <= numGuesses:
            continue
        else:
            topFiveList.pop()
            break
    # This statement can tell if the list has been shortened to four, if so, the players newScore is added to the list
    if len(topFiveList) == 4:
        topFiveList.append(newScore)
    else:
        topFiveList = topFiveList
    print()

    # The list of top 5 scores is printed off now that the game is over.
    print("List of Top Scores:")
    print(topFiveList)
    print()

    # These variables are necessary for storing our updating list back into the text file.
    extraspace = "                  "
    fiveOutList = []
    newScore = ""
    newName = ""

    # This modifies the list to add the extra space back into each line to make it a fixed width file later.
    # This modified list is stored in a new variable, fiveOutList.
    for eachLine in topFiveList:
        [score, name] = eachLine
        newScore = str(score) + extraspace
        newScore = newScore[0:10]
        newName = name + extraspace
        newName = newName[0:25]
        eachLine = [newScore, newName]
        fiveOutList.append(eachLine)

    # this creates a file hand for writing the list back into the text file, then, it writes it into the text file.
    with open("topPlayers.txt", mode="w") as sendingOut:
        for sublist in fiveOutList:
            sendingOut.write("".join(sublist) + "\n")
    #this closes the writing session
    sendingOut.closed

    #this asks the player if they want to play again
    playAgain = input("press Y to play again, N to quit   ")

    #this restarts the game or ends the game depending on if the player enter y or n.  If they don't enter either,
    #the player is notified, and prompted to enter a y or n.
    while True:

        if playAgain.upper() == "Y":
            playGame()
        elif playAgain.upper() == "N":
            print()
            print("thank you for playing")
            quit()
        else:
            print("you didn't enter Y or N")
            print()
            playAgain = input("press Y to play again, N to quit   ")
            print()
