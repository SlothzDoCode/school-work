class battleShips():
    def __init__(self):
        self.board = [None] * 100

class board(battleShips):    
    def __init__(self):
        super().__init__()

    def showBoard(self):
        print(self.board)

