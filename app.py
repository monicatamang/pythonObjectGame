import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")
print("Collect coins ('C') in the maze but watch out for enemies ('E')!")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()

# Create a new Player called played starting at position 21,12
played = player.Player(21,12)

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    board.trackCoins(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")

    # TODO

    # Move the player through the board

    # If the player does not encounter a "wall", move the player in the specified direction
    # If the player encounters an "enemy", the player "dies" and the game ends

    if(selection == "w"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveUp()

        checkPlayerEnemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(checkPlayerEnemy == True):
            print("You lose!")
            break

    elif(selection == "s"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveDown()

        checkPlayerEnemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(checkPlayerEnemy == True):
            print("You lose!")
            break

    elif(selection == "a"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveLeft()

        checkPlayerMove = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(checkPlayerMove == True):
            print("You lose!")
            break
    
    elif(selection == "d"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveRight()

        checkPlayerEnemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(checkPlayerEnemy == True):
            print("You lose!")
            break

    # Check if the player has won, if so print a message and break the loop!
    checkPlayerWin = board.checkWin(played.rowPosition, played.columnPosition)
    if(checkPlayerWin == True):
        print("Congratulations! You win!")
        print(f"Total Coins Collected: {board.coinsCollected}")
        break
