import random

# function to introduce the game and choose the mode playing against the computer or another player
def intro():
    print("Welcome to the game")
    print("Please choose the mode")
    print("1. Play against the computer")
    print("2. Play against another player")
    mode = input("Enter the mode: ")
    # check if the input is correct just for (1 or 2)
    while (mode != "1" and mode != "2"):
        print("Please enter the correct input")
        mode = input("Enter the mode: ")
    # if the mode is 2, ask for the names of the players
    if mode == "2":
        player1 = input("Enter the name of the first player: ")
        player2 = input("Enter the name of the second player: ")
        start = input("Enter the name of the player who starts: ")
    else:
        player1 = "Computer"
        player2 = "User"
        start = "User"
    # explain the rules of the game
    print("The rules of the game are:")
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("Paper beats rock")
    print("If both players choose the same object, it's a tie")
    print("The first player to win 3 times wins the game")
    print("Good luck!")
    # if the user wants to quit the game
    print("Enter 'exit' to quit the game")
    return mode, player1, player2, start


# function ask for user input
def askUserInput():
    object = input("Enter the object: ").lower()
    # check if the input is correct just for (rock or paper, or scissors)
    while (object != "rock" and object != "paper" and object != "scissors" and object != "exit"):
        print("Please enter the correct input")
        object = input("Enter the object: ")
    return object


# function to get computer input
def getComputerInput():
    # create a list of objects
    objects = ["rock", "paper", "scissors"]
    # get a random object from the list
    computerObject = random.choice(objects)
    return computerObject


# function to check who wins in each round
def checkWin(p1Object, p2Object, p1Name, p2Name):
    # if both players choose the same object
    if p1Object == p2Object:
        return "tie"
    # if the Player1 chooses rock
    elif p1Object == "rock":
        if p2Object == "scissors":
            return p1Name
        else:
            return p2Name
    # if the Player1 chooses paper
    elif p1Object == "paper":
        if p2Object == "rock":
            return p1Name
        else:
            return p2Name
    # if the user chooses scissors
    elif p1Object == "scissors":
        if p2Object == "paper":
            return p1Name
        else:
            return p2Name


# Function to count the number of wins for each player
def playerWin(p1Object, p2Object, player1, player2, count1, count2):
    # if the user wins
    if checkWin(p1Object, p2Object, player1, player2) == player1:
        print(player1 + " wins!")
        count1 = count1 + 1
    # if the computer wins
    elif checkWin(p1Object, p2Object, player1, player2) == player2:
        print(player2 + " wins!")
        count2 = count2 + 1
    # if it's a tie
    else:
        print("It's a tie!")

    print("The score is: " + player1 + ": " + str(count1) + " - " + player2 + ": " + str(count2))
    return count1, count2

# function to run the game
def run():
    mode, p1Name, p2Name, start = intro()
    count1 = 0
    count2 = 0
    if mode == "1":
        while True:
            p1Name = "Machine"
            p2Name = "You"
            p2Object = askUserInput()
            if p2Object == 'exit':
                break
            p1Object = getComputerInput()
            print(f'{p1Name} chose: {p1Object}')
            print(f'{p2Name} chose: {p2Object}')
            count1, count2 = playerWin(p1Object, p2Object, p1Name, p2Name, count1, count2)
            # if one of the players wins 3 times
            if count1 == 3:
                print(p1Name + " wins the game!")
                break
            elif count2 == 3:
                print(p2Name + " wins the game!")
                break
            else:
                print("Let's play again!")
    
    elif mode == "2":
        while True:
            if start == p1Name:
                userObject = askUserInput()
                if userObject.lower() == 'exit':
                    break
                computerObject = getComputerInput()
                print("The computer chose: " + computerObject)
                print("You chose: " + userObject)
                playerWin(userObject, computerObject, p1Name, p2Name, count1, count2)
            else:
                computerObject = getComputerInput()
                print("The computer chose: " + computerObject)
                userObject = askUserInput()
                if userObject.lower() == 'exit':
                    break
                print("You chose: " + userObject)
                playerWin(userObject, computerObject, p1Name, p2Name, count1, count2)
    else:
        print("Please enter the correct input")


# code block if main
if __name__ == '__main__':
    run()