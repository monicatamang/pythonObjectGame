class GameBoard:
    def __init__(self):
        self.coinsCollected = 0
        self.winningRow = 0
        self.winningColumn = 6
        self.board = [
            [" * ", " * ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
            [
                " * ",
                " E ",
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
                " E ",
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
                " E ",
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
                " E ",
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
                " E ",
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
                " E ",
                " * "
            ],
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * "]
        ]

    # Printing the gameboard and the player's avatar
    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # end= appends a new space
                # Print the player's avatar if the player is at a certain position on the board and if not, print a "wall"
                if i == playerRow and j == playerColumn:
                    print("P", end="")
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

    # If the player finds a "coin", print the current amount of coins the player has and "delete" the coin
    def trackCoins(self, playerRow, playerColumn):
        if(self.board[playerRow][playerColumn].find("C") != -1):
            self.coinsCollected = self.coinsCollected + 1
            print(f"Coins Collected: {self.coinsCollected}")
            self.board[playerRow][playerColumn] = ""

    # Checking if the player has encountered an "enemy"
    def checkEnemies(self, playerRow, playerColumn):
        if(self.board[playerRow][playerColumn].find("E") != -1):
            return True
        return False

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if(playerRow == self.winningRow and playerColumn == self.winningColumn):
            return True
        else:
            return False