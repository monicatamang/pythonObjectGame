import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")
print("Coins: C")
# print("Enemies: E")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()

# Create a new Player called played starting at position 3,2
# played = player.Player(3,2)
played = player.Player(20,2)

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
        # else:
        #     played = player.Player(3,2)

    elif(selection == "s"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveDown()
        # else:
        #     played = player.Player(3,2)
    
    elif(selection == "a"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveLeft()
        # else:
        #     played = player.Player(3,2)
    
    elif(selection == "d"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveRight()
        # else:
        #     played = player.Player(3,2)

    # Check if the player has won, if so print a message and break the loop!
    check_player_win = board.checkWin(played.rowPosition, played.columnPosition)
    if(check_player_win == True):
        print("Congratulations! You have won the game!")
        print(f"Total Coins Collected: {board.coinsCollected}")
        break
