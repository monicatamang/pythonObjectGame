import gameboard
import player
import enemy

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
played = player.Player(21,12)
enemy_one = enemy.Enemy(19,14)
enemy_two = enemy.Enemy(13,1)
enemy_three = enemy.Enemy(13,14)

# def enemy_one_move():
#     enemy_one_random_move = enemy_one.selectRandomMove()
#     if(enemy_one_random_move == 1):
#         enemy_one.moveUp()
#     elif(enemy_one_random_move == 2):
#         enemy_one.moveDown()
#     elif(enemy_one_random_move == 3):
#         enemy_one.moveLeft()
#     elif(enemy_one_random_move == 4):
#         enemy_one.moveRight()

# def enemy_two_move():
#     enemy_two_random_move = enemy_two.selectRandomMove()
#     if(enemy_two_random_move == 1):
#         enemy_two.moveUp()
#     elif(enemy_two_random_move == 2):
#         enemy_two.moveDown()
#     elif(enemy_two_random_move == 3):
#         enemy_two.moveLeft()
#     elif(enemy_two_random_move == 4):
#         enemy_two.moveRight()

# def enemy_three_move():
#     enemy_three_random_move = enemy_three.selectRandomMove()
#     if(enemy_three_random_move == 1):
#         enemy_three.moveUp()
#     elif(enemy_three_random_move == 2):
#         enemy_three.moveDown()
#     elif(enemy_three_random_move == 3):
#         enemy_three.moveLeft()
#     elif(enemy_three_random_move == 4):
#         enemy_three.moveRight()

while True:
    board.printBoard(played.rowPosition, played.columnPosition, enemy_one.rowPosition, enemy_one.columnPosition, enemy_two.rowPosition, enemy_two.columnPosition, enemy_three.rowPosition, enemy_three.columnPosition,)
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
        # else:
        #     check_enemy_one_move = board.checkEnemyMove(enemy_one.rowPosition, enemy_one.columnPosition)
        #     check_enemy_two_move = board.checkEnemyMove(enemy_two.rowPosition, enemy_two.columnPosition)
        #     check_enemy_three_move = board.checkEnemyMove(enemy_three.rowPosition, enemy_three.columnPosition)
        #     if(check_enemy_one_move == True):
        #         enemy_one_move()
        #     if(check_enemy_two_move == True):
        #         enemy_two_move()
        #     if(check_enemy_three_move == True):
        #         enemy_three_move()

    elif(selection == "s"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveDown()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break
        # else:
        #     check_enemy_one_move = board.checkEnemyMove(enemy_one.rowPosition, enemy_one.columnPosition)
        #     check_enemy_two_move = board.checkEnemyMove(enemy_two.rowPosition, enemy_two.columnPosition)
        #     check_enemy_three_move = board.checkEnemyMove(enemy_three.rowPosition, enemy_three.columnPosition)
        #     if(check_enemy_one_move == True):
        #         enemy_one_move()
        #     if(check_enemy_two_move == True):
        #         enemy_two_move()
        #     if(check_enemy_three_move == True):
        #         enemy_three_move()

    elif(selection == "a"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveLeft()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break
        # else:
        #     check_enemy_one_move = board.checkEnemyMove(enemy_one.rowPosition, enemy_one.columnPosition)
        #     check_enemy_two_move = board.checkEnemyMove(enemy_two.rowPosition, enemy_two.columnPosition)
        #     check_enemy_three_move = board.checkEnemyMove(enemy_three.rowPosition, enemy_three.columnPosition)
        #     if(check_enemy_one_move == True):
        #         enemy_one_move()
        #     if(check_enemy_two_move == True):
        #         enemy_two_move()
        #     if(check_enemy_three_move == True):
        #         enemy_three_move()
    
    elif(selection == "d"):
        check_player_move = board.checkMove(played.rowPosition, played.columnPosition)
        if(check_player_move == True):
            played.moveRight()

        check_player_enemy = board.checkEnemies(played.rowPosition, played.columnPosition)
        if(check_player_enemy == False):
            print("You lose!")
            break
        # else:
        #     check_enemy_one_move = board.checkEnemyMove(enemy_one.rowPosition, enemy_one.columnPosition)
        #     check_enemy_two_move = board.checkEnemyMove(enemy_two.rowPosition, enemy_two.columnPosition)
        #     check_enemy_three_move = board.checkEnemyMove(enemy_three.rowPosition, enemy_three.columnPosition)
        #     if(check_enemy_one_move == True):
        #         enemy_one_move()
        #     if(check_enemy_two_move == True):
        #         enemy_two_move()
        #     if(check_enemy_three_move == True):
        #         enemy_three_move()

    # Check if the player has won, if so print a message and break the loop!
    check_player_win = board.checkWin(played.rowPosition, played.columnPosition)
    if(check_player_win == True):
        print("Congratulations! You win!")
        print(f"Total Coins Collected: {board.coinsCollected}")
        break
