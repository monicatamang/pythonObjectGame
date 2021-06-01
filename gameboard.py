from enemy import Enemy

class GameBoard:
    def __init__(self):
        self.coinsCollected = 0
        self.winningRow = 0
        self.winningColumn = 6
        self.board = [
            [" * ", " * ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
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
                " C ",
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
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * "]
        ]

    def printBoard(self, playerRow, playerColumn, enemyOneRow, enemyOneColumn, enemyTwoRow, enemyTwoColumn, enemyThreeRow, enemyThreeColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # end= appends a new space
                if i == playerRow and j == playerColumn:
                    print("P", end="")
                elif(i == enemyOneRow and j == enemyOneColumn):
                    print("E", end="")
                elif(i == enemyTwoRow and j == enemyTwoColumn):
                    print("E", end="")
                elif(i == enemyThreeRow and j == enemyThreeColumn):
                    print("E", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        # find() returns -1 if the value is not found
        # If the player "hits" a wall, print a message to the player
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True
    
    # def checkEnemyMove(self, enemyTestRow, enemyTestColumn):
    #     for i in range(len(self.board)):
    #         for j in range(len(self.board[i])):
    #             if ((self.board[enemyTestRow][enemyTestColumn].find("*") != -1) or (self.board[enemyTestRow][enemyTestColumn].find("C") != -1) or (self.board[enemyTestRow][enemyTestColumn].find("E") != -1)):
    #                 self.board[enemyTestRow][enemyTestColumn] = self.board[enemyTestRow + 1][enemyTestColumn + 1]
    #                 return False
    #             return True

    def trackCoins(self, playerRow, playerColumn):
        if(self.board[playerRow][playerColumn].find("C") != -1):
            self.coinsCollected = self.coinsCollected + 1
            print(f"Coins Collected: {self.coinsCollected}")
            self.board[playerRow][playerColumn] = ""

    def checkEnemies(self, playerRow, playerColumn):
        if(self.board[playerRow][playerColumn].find("E") != -1):
            return False
        return True

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if(playerRow == self.winningRow and playerColumn == self.winningColumn):
            return True
        else:
            return False
