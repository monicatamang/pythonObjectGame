import random

class Enemy:
    # Creating the constructor which initializes the enemy's row and column position
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # Moving the enemy up
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1

    # Moving the enemy down
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1

    # Moving the enemy left
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1

    # Moving the enemy right
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1

    # Checking if the enemy has "attacked" the player
    def checkEnemyAttack(self, playerRow, playerColumn):
        if(self.rowPosition == playerRow and self.columnPosition == playerColumn):
            return True
        return False

    # Randomly moving the enemy in the maze
    def moveEnemy(self, boardTest):
        # Using the "random" library, generate a random integer from 1 to 4
        randomMove = random.randint(1,4)

        # If "1" is generated, check to see if there is a wall or another enemy above the enemy's current row position. If there are no walls or enemies, move the enemy up
        if(randomMove == 1):
            moveEnemyPosition = boardTest.checkEnemyMove(self.rowPosition - 1, self.columnPosition)
            if(moveEnemyPosition == True):
                self.moveUp()

        # If "2" is generated, check to see if there is a wall or another enemy below the enemy's current row position. If there are no walls or enemies, move the enemy down
        elif(randomMove == 2):
            moveEnemyPosition = boardTest.checkEnemyMove(self.rowPosition + 1, self.columnPosition)
            if(moveEnemyPosition == True):
                self.moveDown()

        # If "3" is generated, check to see if there is a wall or another enemy to the left of the enemy's current column position. If there are no walls or enemies, move the enemy to the left
        elif(randomMove == 3):
            moveEnemyPosition = boardTest.checkEnemyMove(self.rowPosition, self.columnPosition - 1)
            if(moveEnemyPosition == True):
                self.moveLeft()
        
        # If "4" is generated, check to see if there is a wall or another enemy to the right of the enemy's current column position. If there are no walls or enemies, move the enemy to the right
        elif(randomMove == 4):
            moveEnemyPosition = boardTest.checkEnemyMove(self.rowPosition, self.columnPosition + 1)
            if(moveEnemyPosition == True):
                self.moveRight()