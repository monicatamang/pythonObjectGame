class GameBoard:
    # Creating the constructor which initializes the amount of coins the player has, the winning row and column and the maze itself
    # Adding coins directly into the maze
    def __init__(self):
        self.coinsCollected = 0
        self.winningRow = 0
        self.winningColumn = 11
        self.board = [
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * ", " * "],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " C ",
                " C ",
                " C ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                " * ",
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                " * ",
                "   ",
                " * ",
                "   ",
                " * ",
                " C ",
                " * ",
                "   ",
                " * ",
                "   ",
                " * ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                " C ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " C ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "]
        ]

    # Printing the maze
    def printBoard(self, playerRow, playerColumn, enemyOneRow, enemyOneColumn, enemyTwoRow, enemyTwoColumn, enemyThreeRow, enemyThreeColumn):
        # For every column, in every row, if the player and enemies are in their current position, print the player's avatar and each enemy's avatar. If not, print out the other elements in the maze
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # end="" does not print a new line
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                elif(i == enemyOneRow and j == enemyOneColumn):
                    print(" E ", end="")
                elif(i == enemyTwoRow and j == enemyTwoColumn):
                    print(" E ", end="")
                elif(i == enemyThreeRow and j == enemyThreeColumn):
                    print(" E ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    # If the player "hits" a wall, print a message to the player
    def checkMove(self, testRow, testColumn):
        # find() returns -1 if the value is not found
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True
    
    # If the enemy "hits" a wall or another enemy, return "False"
    def checkEnemyMove(self, testRow, testColumn):
        if(self.board[testRow][testColumn].find("*") != -1 or self.board[testRow][testColumn].find("E") != -1):
            return False
        return True

    # If the player finds a "coin", print the current amount of coins the player has and "delete" the coin
    def trackCoins(self, playerRow, playerColumn):
        if(self.board[playerRow][playerColumn].find("C") != -1):
            self.coinsCollected = self.coinsCollected + 1
            print(f"Coins Collected: {self.coinsCollected}")
            self.board[playerRow][playerColumn] = ""

    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if(playerRow == self.winningRow and playerColumn == self.winningColumn):
            return True
        else:
            return False