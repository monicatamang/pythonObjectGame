class Player:
    # Creating the constructor which initializes the player's row and column position
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # Moving the player up
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1

    # Moving the player down
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1

    # Moving the player to the left
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1

    # Moving the player to the right
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1