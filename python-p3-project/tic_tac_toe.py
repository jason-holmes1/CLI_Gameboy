
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = []
        self.current_player = None
        self.winner = None

    def add_player(self, player):
        self.players.append(player)
    
    def start_game(self):
        self.current_player = self.players[0]

    def print_board(self):
        print("This is Connect four. choose A column to place your piece")
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_winner(self):
        #! Check rows for win
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return True
        #! Check columns for win
        for col in range(len(self.board)):
            check = []
            for row in self.board:
                check.append(row[col])
            if check.count(check[0]) == len(check) and check[0] != ' ':
                return True
        #! Check  diagonals for win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player.symbol
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]
            return True
        return False

    def play(self):
        player1_name = input("Enter name for Player 1: ")
        player1_symbol = input("Enter symbol for Player 1: ")
        player1 = Player(player1_name, player1_symbol)
        self.add_player(player1)

        player2_name = input("Enter name for Player 2: ")
        player2_symbol = input("Enter symbol for Player 2: ")
        player2 = Player(player2_name, player2_symbol)
        self.add_player(player2)

        self.start_game()
        while self.winner is None and not self.is_board_full():
            self.print_board()
            row = int(input(f"{self.current_player.name}, enter row: "))
            col = int(input(f"{self.current_player.name}, enter column: "))
            if not self.make_move(row, col):
                print("Invalid move. Try again.")
        self.print_board()
        if self.winner:
            print(f"{self.winner.name} wins!")
        else:
            print("It's a draw.")

if __name__ == "__main__": #? This is used to run the code only if the file is run directly and not imported
    game = TicTacToe()
    game.play()
