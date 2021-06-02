import gameboard
import player
import enemy
import random

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
enemyOne = enemy.Enemy(20,3)
enemyTwo = enemy.Enemy(20,11)
enemyThree = enemy.Enemy(13,14)

def moveEnemyOne():
    randomMove = random.randint(1,4)
    print(f"EnemyOne's Random Number {randomMove}")
    if(randomMove == 1):
        checkEnemyOneMove = board.checkEnemyMove(enemyOne.rowPosition - 1, enemyOne.columnPosition)
        if(checkEnemyOneMove == True):
            enemyOne.moveUp()
        else:
            checkEnemyOneMove = board.checkEnemyMove(enemyOne.rowPosition + 1, enemyOne.columnPosition)
    elif(randomMove == 2):
        checkEnemyOneMove = board.checkEnemyMove(enemyOne.rowPosition + 1, enemyOne.columnPosition, enemyOne.rowPosition, enemyOne.columnPosition)
        if(checkEnemyOneMove == True):
            enemyOne.moveDown()
    elif(randomMove == 3):
        checkEnemyOneMove = board.checkEnemyMove(enemyOne.rowPosition, enemyOne.columnPosition - 1, enemyOne.rowPosition, enemyOne.columnPosition)
        if(checkEnemyOneMove == True):
            enemyOne.moveLeft()
    elif(randomMove == 4):
        checkEnemyOneMove = board.checkEnemyMove(enemyOne.rowPosition, enemyOne.columnPosition + 1, enemyOne.rowPosition, enemyOne.columnPosition)
        if(checkEnemyOneMove == True):
            enemyOne.moveRight()

def moveEnemyTwo():
    randomMove = random.randint(1,4)
    print(f"EnemyTwo's Random Number {randomMove}")
    if(randomMove == 1):
        checkEnemyTwoMove = board.checkEnemyMove(enemyTwo.rowPosition - 1, enemyTwo.columnPosition, enemyTwo.rowPosition, enemyTwo.columnPosition)
        if(checkEnemyTwoMove == True):
            enemyTwo.moveUp()
    elif(randomMove == 2):
        checkEnemyTwoMove = board.checkEnemyMove(enemyTwo.rowPosition - 1, enemyTwo.columnPosition, enemyTwo.rowPosition, enemyTwo.columnPosition)
        if(checkEnemyTwoMove == True):
            enemyTwo.moveDown()
    elif(randomMove == 3):
        checkEnemyTwoMove = board.checkEnemyMove(enemyTwo.rowPosition - 1, enemyTwo.columnPosition, enemyTwo.rowPosition, enemyTwo.columnPosition)
        if(checkEnemyTwoMove == True):
            enemyTwo.moveLeft()
    elif(randomMove == 4):
        checkEnemyTwoMove = board.checkEnemyMove(enemyTwo.rowPosition - 1, enemyTwo.columnPosition, enemyTwo.rowPosition, enemyTwo.columnPosition)
        if(checkEnemyTwoMove == True):
            enemyTwo.moveRight()

def moveEnemyThree():
    randomMove = random.randint(1,4)
    print(f"EnemyThree's Random Number {randomMove}")
    if(randomMove == 1):
        checkEnemyThreeMove = board.checkEnemyMove(enemyThree.rowPosition - 1, enemyThree.columnPosition, enemyThree.rowPosition, enemyThree.columnPosition)
        if(checkEnemyThreeMove == True):
            enemyThree.moveUp()
    elif(randomMove == 2):
        checkEnemyThreeMove = board.checkEnemyMove(enemyThree.rowPosition - 1, enemyThree.columnPosition, enemyThree.rowPosition, enemyThree.columnPosition)
        if(checkEnemyThreeMove == True):
            enemyThree.moveDown()
    elif(randomMove == 3):
        checkEnemyThreeMove = board.checkEnemyMove(enemyThree.rowPosition - 1, enemyThree.columnPosition, enemyThree.rowPosition, enemyThree.columnPosition)
        if(checkEnemyThreeMove == True):
            enemyThree.moveLeft()
    elif(randomMove == 4):
        checkEnemyThreeMove = board.checkEnemyMove(enemyThree.rowPosition - 1, enemyThree.columnPosition, enemyThree.rowPosition, enemyThree.columnPosition)
        if(checkEnemyThreeMove == True):
            enemyThree.moveRight()

while True:
    board.printBoard(played.rowPosition, played.columnPosition, enemyOne.rowPosition, enemyOne.columnPosition, enemyTwo.rowPosition, enemyTwo.columnPosition, enemyThree.rowPosition, enemyThree.columnPosition)
    board.trackCoins(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")

    # TODO

    # Move the player through the board

    # If the player does not encounter a "wall", move the player in the specified direction
    # If the player encounters an "enemy", the player "dies" and the game ends

    if(selection == "w"):
        checkPlayerMove = board.checkMove(played.rowPosition - 1, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveUp()

        moveEnemyOne()
        moveEnemyTwo()
        moveEnemyThree()

        enemyOneAttackPlayer = enemyOne.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyTwoAttackPlayer = enemyTwo.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyThreeAttackPlayer = enemyThree.checkEnemyAttack(played.rowPosition, played.columnPosition)

        if(enemyOneAttackPlayer == True or enemyTwoAttackPlayer == True or enemyThreeAttackPlayer == True):
            print("You lose!")
            break


    elif(selection == "s"):
        checkPlayerMove = board.checkMove(played.rowPosition + 1, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveDown()

        moveEnemyOne()
        moveEnemyTwo()
        moveEnemyThree()

        enemyOneAttackPlayer = enemyOne.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyTwoAttackPlayer = enemyTwo.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyThreeAttackPlayer = enemyThree.checkEnemyAttack(played.rowPosition, played.columnPosition)

        if(enemyOneAttackPlayer == True or enemyTwoAttackPlayer == True or enemyThreeAttackPlayer == True):
            print("You lose!")
            break


    elif(selection == "a"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition - 1)
        if(checkPlayerMove == True):
            played.moveLeft()

        moveEnemyOne()
        moveEnemyTwo()
        moveEnemyThree()

        enemyOneAttackPlayer = enemyOne.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyTwoAttackPlayer = enemyTwo.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyThreeAttackPlayer = enemyThree.checkEnemyAttack(played.rowPosition, played.columnPosition)

        if(enemyOneAttackPlayer == True or enemyTwoAttackPlayer == True or enemyThreeAttackPlayer == True):
            print("You lose!")
            break
    
    elif(selection == "d"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition + 1)
        if(checkPlayerMove == True):
            played.moveRight()

        moveEnemyOne()
        moveEnemyTwo()
        moveEnemyThree()

        enemyOneAttackPlayer = enemyOne.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyTwoAttackPlayer = enemyTwo.checkEnemyAttack(played.rowPosition, played.columnPosition)
        enemyThreeAttackPlayer = enemyThree.checkEnemyAttack(played.rowPosition, played.columnPosition)

        if(enemyOneAttackPlayer == True or enemyTwoAttackPlayer == True or enemyThreeAttackPlayer == True):
            print("You lose!")
            break

    # Check if the player has won, if so print a message and break the loop!
    checkPlayerWin = board.checkWin(played.rowPosition, played.columnPosition)
    if(checkPlayerWin == True):
        print("Congratulations! You win!")
        print(f"Total Coins Collected: {board.coinsCollected}")
        break
