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

# Create a new Player called played starting at position 3,2
# played = player.Player(3,2)
played = player.Player(21,12)

while True:
    # board.printBoard(player.rowPosition, player.columnPosition)
    board.printBoard(played.rowPosition, played.columnPosition)
    board.trackCoins(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")

    # TODO

    # Move the player through the board
    if(selection == "w"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveUp()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break

    elif(selection == "s"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveDown()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break

    elif(selection == "a"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveLeft()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break
    
    elif(selection == "d"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveRight()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break

    # Check if the player has won, if so print a message and break the loop!
    check_player_win = board.checkWin(played.rowPosition, played.columnPosition)
    if(check_player_win == True):
        print("Congratulations! You win!")
        print(f"Total Coins Collected: {board.coinsCollected}")
        break
