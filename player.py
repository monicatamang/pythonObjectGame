class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1
        print(f"Row: {self.rowPosition}")
    # TODO
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1
        print(f"Row: {self.rowPosition}")

    # TODO
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1
        print(f"Column: {self.columnPosition}")

    # TODO
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1
        print(f"Column: {self.columnPosition}")
