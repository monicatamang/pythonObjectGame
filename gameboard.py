class GameBoard:
    def __init__(self):
        # self.winningRow = 0
        # self.winningColumn = 2
        self.coinsCollected = 0
        self.winningRow = 0
        self.winningColumn = 11
        self.board = [
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * ", " * "],
            [
                " * ",
                " C ",
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
                " E ",
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
                " E ",
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
                " E ",
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
                " E ",
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
                "   ",
                "   ",
                "   ",
                " C ",
                " C ",
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
                " C ",
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
                " E ",
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

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # end= appends a new space
                if i == playerRow and j == playerColumn:
                    print("P", end="")
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
