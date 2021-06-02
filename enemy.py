class Enemy:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1

    # TODO
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1

    # TODO
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1

    # TODO
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1

    # Checking if the player has encountered an "enemy"
    def checkEnemyAttack(self, playerRow, playerColumn):
        if(self.rowPosition == playerRow and self.columnPosition == playerColumn):
            return True
        return False