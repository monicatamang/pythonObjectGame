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

# Creating a new GameBoard called board
board = gameboard.GameBoard()

# Creating a new Player called played starting at position 20,12 and creating three enemies at different positions in the maze
played = player.Player(20,12)
enemyOne = enemy.Enemy(20,3)
enemyTwo = enemy.Enemy(20,14)
enemyThree = enemy.Enemy(13,14)

# Moving the enemies based on the structure of the maze
def movingEnemy():
    enemyOne.moveEnemy(board)
    enemyTwo.moveEnemy(board)
    enemyThree.moveEnemy(board)

# Checking if any enemies has "attacked" the player, given the player's current row and column
def enemyAttack():
    enemyOneAttackPlayer = enemyOne.checkEnemyAttack(played.rowPosition, played.columnPosition)
    enemyTwoAttackPlayer = enemyTwo.checkEnemyAttack(played.rowPosition, played.columnPosition)
    enemyThreeAttackPlayer = enemyThree.checkEnemyAttack(played.rowPosition, played.columnPosition)

    # If an enemy does "attack" the player, the player loses the game. If not, the player can continue playing the game
    if(enemyOneAttackPlayer == True or enemyTwoAttackPlayer == True or enemyThreeAttackPlayer == True):
        print("You lose!")
        return True
    return False

while True:
    # Printing the maze based on the player's current row and column and each enemy's current row and column
    board.printBoard(played.rowPosition, played.columnPosition, enemyOne.rowPosition, enemyOne.columnPosition, enemyTwo.rowPosition, enemyTwo.columnPosition, enemyThree.rowPosition, enemyThree.columnPosition)

    # Tracking the current number of coins the player has collected in the maze
    board.trackCoins(played.rowPosition, played.columnPosition)

    # Prompting the user to make a move
    selection = input("Make a move: ")

    # Moving the enemy to a new position in the maze
    movingEnemy()
    
    # Checking to see if the enemy "attacks" a player. If the enemy does "attack" the player, end the game
    enemyAttackPlayer = enemyAttack()
    if(enemyAttackPlayer == True):
        break
        
    # If the player wants to move up, check if there's a wall. If there is no wall, move the player up
    if(selection == "w"):
        checkPlayerMove = board.checkMove(played.rowPosition - 1, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveUp()

    # If the player wants to move down, check if there's a wall. If there is no wall, move the player down
    elif(selection == "s"):
        checkPlayerMove = board.checkMove(played.rowPosition + 1, played.columnPosition)
        if(checkPlayerMove == True):
            played.moveDown()

    # If the player wants to move left, check if there's a wall. If there is no wall, move the player to the left
    elif(selection == "a"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition - 1)
        if(checkPlayerMove == True):
            played.moveLeft()

    # If the player wants to move right, check if there's a wall. If there is no wall, move the player to the right
    elif(selection == "d"):
        checkPlayerMove = board.checkMove(played.rowPosition, played.columnPosition + 1)
        if(checkPlayerMove == True):
            played.moveRight()

    # Check if the player has won, if so print a message and break the loop!
    # Printing the total amount of coins the player has collected in the maze
    checkPlayerWin = board.checkWin(played.rowPosition, played.columnPosition)
    if(checkPlayerWin == True):
        print("Congratulations! You win!")
        print(f"Total Coins Collected: {board.coinsCollected}")
        break