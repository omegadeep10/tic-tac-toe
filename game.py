class TicTacToe:

    def __init__(self):
        self.board = ["O", " ", "X", 
                      "X", " ", " ", 
                      "X", "O", "O"]

    def show(self):
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def availableMoves(self):
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getSquares(self, player):
        squares = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                squares.append(i)
        return squares

    def checkWin(self):
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getSquares(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True






if __name__ == '__main__':
    game = TicTacToe()
    game.show()
    print(game.gameOver())