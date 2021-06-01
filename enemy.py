import random

class Enemy:
    def __init__(self, intitalRow, initialColumn):
        self.startPositionRow = intitalRow
        self.startPositionCol = initialColumn
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1
        print(f"EnemyRow: {self.rowPosition}")

    # TODO
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1
        print(f"EnemyRow: {self.rowPosition}")

    # TODO
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1
        print(f"EnemyColumn: {self.columnPosition}")

    # TODO
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1
        print(f"EnemyColumn: {self.columnPosition}")

    def selectRandomMove(self):
        random_value = random.randint(1,4)
        return random_value